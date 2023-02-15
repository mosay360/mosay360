"""mosay360 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from django.contrib import admin
from  members.forms import LoginForm
from members.views import CustomLoginView, ResetPasswordView, ChangePasswordView
from django.urls import path, include, re_path

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include ('home.urls')),
    
    path('blog/', include('blog.urls', namespace='blog')),
    path("i18n/", include("django.conf.urls.i18n")),
    
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='registration/login.html',
                                           authentication_form=LoginForm), name='login'),

    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),

    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),

    path('password-change/', ChangePasswordView.as_view(), name='password_change'),

    re_path(r'^oauth/', include('social_django.urls', namespace='social')),

]
urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


