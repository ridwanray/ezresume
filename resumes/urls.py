from django.urls import path

from . import views
from users import views as user_views

urlpatterns = [
    path('', views.my_resumes, name='my-resumes'),
    path('edit-profile/', views.edit_profile, name='edit-profile'),
    path('delete/<int:pk>/', views.delete_resume, name='delete-resume'),
    path('resume/create/', views.ResumeWizard.as_view(views.FORMS), name='create-resume'),
    path('edit/resume/<int:pk>/', views.ResumeWizard.as_view(views.FORMS), name='edit-resume'),
    path('faq/', views.faq, name='faq'),
    path('templates/', views.templates, name='templates'),
    path('payment/', user_views.payment, name='payment'),
    path('payment/notification/', user_views.payment_notification, name='payment-notif'),
    path('resume/<int:pk>/choose/', views.choose, name='choose'),
    path('resume/<int:pk>/view-resume/', views.choose, name='view-resume'),
]
