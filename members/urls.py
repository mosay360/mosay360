from django.urls import path
from .views import  profile, RegisterView

urlpatterns =[
    #path('register/', UserRegisterView.as_view(),name='register'),
    
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', profile, name='profile'),
]