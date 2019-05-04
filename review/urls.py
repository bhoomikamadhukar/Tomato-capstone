from django.urls import path
from review.views import *
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
	path('',home),
	path('institute/<int:institution_id>/',institution),
	path('institute/<int:inst_id>/department/',teachers),
	path('institute_feedback/<int:institution_id>/',institution_review),
	path('teacher/<int:teacher_id>/',teacher_review),
    path('teacher_feedback/<int:teacher_id>/',teacher_review),
    path('login/',signin),
    path('logout/',signout),
    path('signup/',signup),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
