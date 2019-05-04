from django.shortcuts import render, redirect
from datetime import datetime
from .models import *
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User


def home(request):
	all_institutions = Institution.objects.all()
	popular = all_institutions.filter(average_rating__gte = 4)
	others = all_institutions.filter(average_rating__lte=3)
	return render(request,"index.html",{'popular':popular,'others':others})



def institution(request,institution_id):
	institution=Institution.objects.get(id=institution_id)
	institution_feedback=InstitutionFeedback.objects.filter(institution=institution)
	print(institution_feedback)
	return render(request,'institute.html',{'institution':institution,'institution_feedback':institution_feedback})

def teachers(request,inst_id):
	institution = Institution.objects.get(pk = inst_id)
	teacher_institute=Teacher.objects.filter(institute=institution)

	if request.method=="POST":
		name=request.POST.get("department")	
		if name != "All":
			teacher_institute=Teacher.objects.filter(department=name,institute=institution)
		
	return render(request,'teacher.html',{'teacher_institute':teacher_institute, "institution": institution})


def institution_review(request,institution_id):
	if request.method=="POST":
		user=request.user
		infrastructure=int(request.POST.get("infrastructure"))
		placements=int(request.POST.get("placements"))
		faculty=int(request.POST.get("faculty"))
		management=int(request.POST.get("management"))
		comments=request.POST.get("comment")
		institution=Institution.objects.get(id=institution_id)
		feedback=InstitutionFeedback(user=user,
							institution=institution,
							infrastructure=int(infrastructure),
							placements=int(placements),
							faculty=int(faculty),
							management=int(management),
							comments=comments)
		feedback.save()
		number_of_feedbacks = len(InstitutionFeedback.objects.filter(institution=institution))-1
		print(number_of_feedbacks)
		print(type(institution.infrastructure))
		infrastructure_rating=((int(institution.infrastructure)*number_of_feedbacks)+int(infrastructure))/(number_of_feedbacks+1)
		print(type(infrastructure_rating))
		placement_rating=((int(institution.placements)*number_of_feedbacks)+int(placements))/(number_of_feedbacks+1)
		faculty_rating=((int(institution.faculty)*number_of_feedbacks)+int(faculty))/(number_of_feedbacks+1)
		management_rating=((int(institution.management)*number_of_feedbacks)+int(management))/(number_of_feedbacks+1)
		institution.infrastructure=infrastructure_rating
		institution.placements=placement_rating
		institution.faculty=faculty_rating
		institution.management=management_rating
		avg = (infrastructure_rating+placement_rating+faculty_rating+management_rating)/4
		institution.average_rating = avg
		print(avg)
		institution.save()
		return redirect(f"/institute/{institution_id}/")
	
	return render(request,"institution_feedback_form.html",{"institution_id":institution_id})


def teacher_review(request, teacher_id):
	teacher = Teacher.objects.get(pk=teacher_id)
	reviews = TeacherFeedback.objects.filter(teacher=teacher)
	if request.method=="POST":
		user = request.user
		rating = request.POST.get("rating")
		comments=request.POST.get("comment")
		teacher = Teacher.objects.get(id=teacher_id)
		feedback = TeacherFeedback(user=user, teacher=teacher, rating=int(rating), comments=comments)
		feedback.save()
		current_rating = teacher.rating
		number_of_feedbacks = len(TeacherFeedback.objects.filter(teacher=teacher))-1
		new_rating = ((current_rating * number_of_feedbacks ) + int(rating))/(number_of_feedbacks+1)
		print(new_rating)
		teacher.rating = new_rating
		teacher.save()
		return redirect(f"/teacher/{teacher_id}/")

	return render(request,"teacher_feedback_form.html",{"teacher":teacher, "reviews":reviews})

def signin(request):
	if request.method=='POST':
		username=request.POST.get('username',None)
		password=request.POST.get('password',None)
		user=authenticate(request,username=username,password=password)
		if user is not None:
			print("Im in")
			login(request,user)
			return redirect("/")
	return render(request,"login.html")



def signup(request):
	if request.method=='POST':
		usn=request.POST.get('usn',None)
		fullname=request.POST.get('fullname',None)
		email=request.POST.get('email',None)
		username=request.POST.get('username',None)
		password=request.POST.get('password',None)

		user_exists=User.objects.filter(username=username)
		if not user_exists:
			user=User.objects.create_user(
				username=username,
				password=password,
				email=email,
				first_name=fullname.split()[0],
				last_name=" ".join(fullname.split()[1:])
				)
			login(request,user)
			return redirect("/")
		else:
			return HttpResponse("Username exists. Try another name")
	return render(request,"signup.html")


def signout(request):
	logout(request)
	return redirect("/")



