from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from users import views as user_views
from . import views
from .sitemap import StaticSitemap

sitemaps = {'pages': StaticSitemap}

urlpatterns = [
    path('app/', include(('resumes.urls', 'resumes'), namespace='resumes')),
    path('accounts/', include('allauth.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    path('', views.home_view, name='home'),
    path('activate/<uidb64>/<token>/', user_views.activate, name='activate'),
    path('payment-notification/', user_views.payment_notification, name='payment-notif'),
    path('privacy/', views.privacy, name='privacy'),
    path('payment-confirmed/', user_views.payment_confirmed, name='payment-confirmed'),
    path('payment-unfinished/', user_views.payment_unfinished, name='payment-unfinished'),
    path('payment-error/', user_views.payment_error, name='payment-error'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    re_path(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: ", mimetype="text/plain")),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
