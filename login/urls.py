from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.login,name='loginPage'),
    path('validateLogin/',views.validateLogin,name='validate'),
]
