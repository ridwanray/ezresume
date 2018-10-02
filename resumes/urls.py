from django.urls import path

from . import views

urlpatterns = [
    path('', views.my_resumes, name='my-resumes'),
    path('create-resume/', views.create_resume, name='create-resume'),
]