from . import views
from django.urls import path,include


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('track/', views.track, name='track'),
    path('adminDashboard', views.adminDashboardRedirect, name='adminDashboardRedirect'),
]
