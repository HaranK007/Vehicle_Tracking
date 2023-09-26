from . import views
from django.urls import path,include

#app_name = 'adminDashboard'

urlpatterns = [
    path('',views.adminDashboard,name='adminDashboard'),
    
    path('user/',views.user,name='user'),
    path('user/edit/<int:rowId>',views.userEdit,name='userEdit'),
    path('user/edit/save/',views.userSave,name='userSave'),
    path('user/delete/',views.userDelete,name='userDelete'),
    path('user/add/',views.userAdd,name='userAdd'),

    path('device/',views.device,name='device'),
    path('device/edit/<int:rowId>',views.deviceEdit,name='deviceEdit'),
    path('device/edit/save/',views.deviceSave,name='deviceSave'),
    path('device/delete/',views.deviceDelete,name='deviceDelete'),
    path('device/add/',views.deviceAdd,name='deviceAdd'),

    path('vehicle/',views.vehicle,name='vehicle'),
    path('vehicle/delete/',views.vehicleDelete,name='vehicleDelete'),
    path('vehicle/edit/<int:rowId>',views.vehicleEdit,name='vehicleEdit'),
    path('vehicle/edit/save/',views.vehicleSave,name='vehicleSave'),
    path('vehicle/add/',views.vehicleAdd,name='vehicleAdd'),


    path('group/',views.group,name='group'),
    path('group/add/',views.groupAdd,name='groupAdd'),
    path('group/delete/',views.groupDelete,name='groupDelete'),
    path('group/edit/<int:rowId>',views.groupEdit,name='groupEdit'),
    path('group/view/<str:groupName>',views.groupView,name='groupView'),
    path('group/view/delete/',views.groupViewDelete,name='groupViewDelete'),
    path('group/edit/save/',views.groupSave,name='groupSave'),

    path('person/',views.person,name='person'),
    path('person/add/',views.personAdd,name='personAdd'),
    path('person/delete/',views.personDelete,name='personDelete'),
    path('person/edit/<int:rowId>',views.personEdit,name='personEdit'),
    path('person/edit/save/',views.personSave,name='personEdit'),
]
