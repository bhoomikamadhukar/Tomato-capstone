from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

DEPT_NAME=(
			('CSE',"Computer Science"),
			('ISE',"Information Science"),
			('ECE',"Electronics and Communication"),
			('EEE',"Electrical and Electronics"),
			('ME',"Mechanical"),
			('CE',"Civil"),
			('TC',"Telecommunication"),
			('BT',"Biotechnology")
			)


class Institution(models.Model):
	name=models.CharField(max_length=100)
	location=models.CharField(max_length=100)
	email=models.EmailField(null=True)
	website=models.CharField(max_length=100)
	cover=models.ImageField(upload_to="all_covers/",default="all_covers/cover.jpg")
	infrastructure = models.IntegerField(default=1)
	placements = models.IntegerField(default=1)
	faculty = models.IntegerField(default=1)
	management = models.IntegerField(default=1)
	average_rating = models.IntegerField(default=1)
	summary = models.CharField(max_length=500)	

	def __str__(self):
		return self.name

	@property
	def rating(self):
		return range(self.average_rating)
	

class Teacher(models.Model):
	institute = models.ForeignKey(Institution, on_delete=models.CASCADE)
	teacher_name=models.CharField(max_length=100)
	email=models.EmailField(null=True)
	phone=models.CharField(max_length=10)
	rating=models.IntegerField(default=1)
	qualification=models.CharField(max_length=100)
	designation=models.CharField(max_length=100)
	department=models.CharField(max_length=3, choices=DEPT_NAME)

	def __str__(self):
		return f" {self.teacher_name}|{self.rating}"

	@property
	def avg_rating(self):
		return range(self.rating)

class InstitutionFeedback(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	institution=models.ForeignKey(Institution,on_delete=models.CASCADE)
	comments=models.CharField(max_length=250)
	timestamp=models.DateTimeField(default=datetime.now)
	infrastructure = models.IntegerField(default=1)
	placements = models.IntegerField(default=1)
	faculty = models.IntegerField(default=1)
	management = models.IntegerField(default=1)

	@property
	def Rinfrastructure(self):
		return range(self.infrastructure)

	@property
	def Rplacements(self):
		return range(self.placements)

	@property
	def Rfaculty(self):
		return range(self.faculty)

	@property
	def Rmanagement(self):
		return range(self.management)
	

	def __str__(self):
		return f"{self.institution}"

class TeacherFeedback(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
	comments=models.CharField(max_length=250)
	timestamp=models.DateTimeField(default=datetime.now)
	rating = models.IntegerField(default=1)
	

	@property
	def avg_rating(self):
		return range(self.rating)
"""
class Department(models.Model): 
	dept_name=models.CharField(choices=DEPT_NAME)
	institution=models.ForeignKey(Institution,on_delete=models.CASCADE)


class Reviews(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
	institution=models.ForeignKey(Institution,on_delete=models.CASCADE)
	rating_institution = models.FloatField(default=0.0, null=True, blank=True)
	rating_tea = models.FloatField(default=0.0, null=True, blank=True)
	
	comments_institution=models.CharField(max_length=100,blank=True,null=True)
	timestamp=models.DateTimeField(default=datetime.now)



	def __str__(self):
		return f" {self.teacher}|{self.rating}"




"""