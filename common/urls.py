from django.urls import path,include
from .views import (RegisterApiView,LoginAPI,UserApiView,
LogoutApiView,ProfileInfoApiView,PasswordApiView)
urlpatterns = [
    path('register',RegisterApiView.as_view()),
    path('login',LoginAPI.as_view()),
    path('user',UserApiView.as_view()),
    path('logout',LogoutApiView.as_view()),
    path('users/info',ProfileInfoApiView.as_view()),
    path('users/password',PasswordApiView.as_view()),
]