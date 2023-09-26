from django.shortcuts import render,redirect
import json
from django.urls import reverse
from django.db import connection
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from adminDashboard.models import Vehicle,Device,Person,Group
from datetime import datetime
from .froms import GroupForm

# Create your views here.

def adminDashboard(request):

    return render(request,'adminDashboard.html')

#user ----------------------------------------------------------------------------------------------------

def user(request):
    print('user clicked')
    users = User.objects.all().values('id', 'username', 'email')
    columns = ["ID", "Username", "Email"]
    popup = False
    print(users)

    return render(request, 'displayTable.html', {'users': users, 'columns': columns, 'popup':popup,'editRow':None })

def userEdit(request,rowId):
    users = User.objects.all().values('id', 'username', 'email')
    editRow = User.objects.filter(id=rowId).values('id', 'username', 'email')
    columns = ["ID", "Username", "Email"]
    popup = True

    return render(request,'displayTable.html',{'users':users,'editRow':editRow, 'columns':columns,'popup':popup})
    
def userSave(request):
    if request.method == 'POST':
        id = request.POST['id']
        name = request.POST['username']
        email = request.POST['email']

        try:

            user = User.objects.get(id=id)

            user.username = name
            user.email = email
            user.save()
            print('updated')
            return redirect('/adminDashboard/user')
        except User.DoesNotExist:
            print("failed")
            return redirect('adminDashboard/')  
    return

def userDelete(request):
    print("delete called")
    if request.method == 'POST':
        data = json.loads(request.body)
        selected_users = data.get('user_ids')
        print(selected_users)
        try:
            User.objects.filter(id__in=selected_users).delete()
            print('Deleted selected users')
        except User.DoesNotExist:
            print('Some selected users do not exist')

        return HttpResponseRedirect(reverse('adminDashboard'))

    return HttpResponseRedirect(reverse('adminDashboard'))

def userAdd(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        new_user = User(username=name, email=email, password= password)
        new_user.save()

        return redirect('/adminDashboard/user/')

# device ----------------------------------------------------------------------------------------------------

def device(request):
    print('device')
    device = Device.objects.all().values('id','device_id','hardware_ver','software_ver','model')
    columns = ['device_id','hardware_ver','software_ver','model']
    popup = False
    print(device)
    return render(request, 'displayDevices.html', {'device': device, 'columns':columns,'popup':popup,'editRow':None})

def deviceDelete(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        selected_users = data.get('user_ids')

        try:
            Device.objects.filter(id__in=selected_users).delete()
            print('Deleted selected users')
        except User.DoesNotExist:
            print('Some selected users do not exist')

        return HttpResponseRedirect(reverse('adminDashboard'))

    return HttpResponseRedirect(reverse('adminDashboard'))

def deviceAdd(request):
    if request.method == 'POST':
        device_id = request.POST['device_id']
        hardware_ver = request.POST['hardware_ver']
        software_ver = request.POST['software_ver']
        model = request.POST['model']

        new_row = Device(device_id=device_id, hardware_ver=hardware_ver, software_ver= software_ver,model=model)
        new_row.save()

        return HttpResponseRedirect(reverse('adminDashboard'))

def deviceEdit(request,rowId):
    device = Device.objects.all().values('id','device_id','hardware_ver','software_ver','model')
    deviceSeclectd = Device.objects.filter(id=rowId).values('id', 'device_id', 'hardware_ver','software_ver','model')
    columns = ["ID", "device_id", "hardware_ver",'software_ver','model']
    popup = True

    return render(request,'displayDevices.html', {'device': device, 'columns':columns,'popup':popup,'editRow':deviceSeclectd})
    
def deviceSave(request):
    if request.method == 'POST':
        id = request.POST['id']
        device_id = request.POST['device_id']
        hardware_ver = request.POST['hardware_ver']
        software_ver = request.POST['software_ver']
        model = request.POST['model']

        try:

            user = Device.objects.get(id=id)

            user.device_id = device_id
            user.hardware_ver = hardware_ver
            user.software_ver = software_ver
            user.model = model
            user.save()
            print('updated')
            return redirect('/adminDashboard/device/')
        except User.DoesNotExist:
            return redirect('adminDashboard/')  
    return

# vehicle ----------------------------------------------------------------------------------------------------

def vehicle(request):

    vehicle = Vehicle.objects.all().values('id','vehicle_no', 'engine_no', 'chassis_no','Fuel','Manufacturer')
    columns = ['vehicle_no', 'engine_no', 'chassis_no','Fuel','Manufacturer']
    popup = False

    return render(request,'displayVehicles.html',{'user':vehicle, 'columns':columns,'popup':popup,'editRow':None})

def vehicleEdit(request,rowId):
    vehicle = Vehicle.objects.all().values('id','vehicle_no', 'engine_no', 'chassis_no','Fuel','Manufacturer')
    vehicleSecleted = Vehicle.objects.filter(id=rowId).values('id','vehicle_no', 'engine_no', 'chassis_no','Fuel','Manufacturer')
    columns = ['vehicle_no', 'engine_no', 'chassis_no','Fuel','Manufacturer']
    popup = True

    return render(request,'displayVehicles.html',{'user':vehicle, 'columns':columns,'popup':popup,'editRow':vehicleSecleted})

def vehicleSave(request):
    if request.method == 'POST':
        id = request.POST['id']
        vehicle_no = request.POST['vehicle_no']
        engine_no = request.POST['engine_no']
        chassis_no = request.POST['chassis_no']
        Fuel = request.POST['Fuel']
        Manufacturer = request.POST['Manufacturer']

        try:

            vehicle = Vehicle.objects.get(id=id)

            vehicle.vehicle_no = vehicle_no
            vehicle.engine_no = engine_no
            vehicle.chassis_no = chassis_no
            vehicle.Fuel = Fuel
            vehicle.Manufacturer = Manufacturer
            vehicle.save()
            print('updated')
            return redirect('/adminDashboard/vehicle/')
        except User.DoesNotExist:
            return HttpResponseRedirect(reverse('adminDashboard'))
    return 

def vehicleAdd(request):
    if request.method == 'POST':
        vehicle_no = request.POST['vehicle_no']
        engine_no = request.POST['engine_no']
        chassis_no = request.POST['chassis_no']
        Manufacturer = request.POST['Manufacturer']
        Fuel_type = request.POST['Fuel']
        Insurance = request.POST['Insurance']
        Fuel_cap = request.POST['Fuel_cap']
        RC = request.POST['RC']

        formatted_RC = datetime.strptime(RC, '%Y-%m-%d').date()
        formatted_Insurance = datetime.strptime(Insurance, '%Y-%m-%d').date()

        new_row = Vehicle(vehicle_no=vehicle_no, engine_no=engine_no, chassis_no= chassis_no,Manufacturer=Manufacturer,Fuel=Fuel_type,Fuel_cap=Fuel_cap,Insurance=formatted_Insurance,RC=formatted_RC)
        new_row.save()

        return redirect('/adminDashboard/vehicle/')
    
def vehicleDelete(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        selected_users = data.get('user_ids')

        try:
            Vehicle.objects.filter(id__in=selected_users).delete()
            print('Deleted selected users')
        except User.DoesNotExist:
            print('Some selected users do not exist')

        return redirect('/adminDashboard/vehicle/')

    return HttpResponseRedirect(reverse('adminDashboard'))

# group ----------------------------------------------------------------------------------------------------

def group(request):
    group = Group.objects.all().values('id','name').distinct('name')
    columns = ['name']
    popup = False

    return render(request, 'displayGroup.html', {'group':group,'columns':columns,'popup':popup,'editRow':None})

def groupEdit(request,rowId):
    group = Group.objects.all().values('id','name')
    groupSelected = Group.objects.filter(id=rowId).values('id', 'name')
    columns = ["ID", "name"]
    popup = True

    return render(request,'displayGroup.html',{'group':group, 'columns':columns,'popup':popup,'editRow':groupSelected})

def groupSave(request):
    if request.method == 'POST':

        id = request.POST['id']
        name = request.POST['name']

        try:

            group = Group.objects.get(id=id)

            group.name = name
            print(group)
            # group.save()
            print('updated')
            return redirect('/adminDashboard/group/')
        except User.DoesNotExist:
            return redirect('/adminDashboard/')  
    return

def groupAdd(request):
    if request.method == 'POST':
        name = request.POST['name']

        new_row = Group(name=name)
        new_row.save()

        return redirect('/adminDashboard/group/')
    
def groupDelete(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        selected_users = data.get('user_ids')

        try:
            Group.objects.filter(id__in=selected_users).delete()
            print('Deleted selected users')
        except Group.DoesNotExist:
            print('Some selected users do not exist')

        return redirect('/adminDashboard/group/')
    
    return HttpResponseRedirect(reverse('adminDashboard'))

def groupView(request,groupName):
    print(groupName)
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., save the group)
            form.save()
            return redirect('/adminDashboard/group/')
    else:
        group = Group.objects.filter(name=groupName).values('id','vheicleId','deviceId','personId','userId')
        columns = ['vheicleId','deviceId','personId','userId']
        form = GroupForm()

        return render(request, 'displayGroupDetails.html', {'group':group,'columns':columns,'form':form})

def groupViewDelete(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        selected_users = data.get('user_ids')

        try:
            Group.objects.filter(id__in=selected_users).delete()
            print('Deleted selected users')
        except Group.DoesNotExist:
            print('Some selected users do not exist')

        return redirect('/adminDashboard/group/')
    
    return HttpResponseRedirect(reverse('adminDashboard'))


    
# person ----------------------------------------------------------------------------------------------------

def person(request):
    person = Person.objects.all().values('id','name','dob','blood_group','licence_no')
    columns = ['name','dob','blood_group','licence_no']
    popup = False

    return render(request, 'displayPerson.html', {'person':person,'columns':columns,'popup':popup,'editRow':None})

def personAdd(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        blood_group = request.POST['blood_group']
        licence_no = request.POST['licence_no']

        new_row = Person(name=name, dob=dob, blood_group= blood_group,licence_no=licence_no)
        new_row.save()

        return redirect('/adminDashboard/person/')
    
def personDelete(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        selected_users = data.get('user_ids')

        try:
            Person.objects.filter(id__in=selected_users).delete()
            print('Deleted selected users')
        except Person.DoesNotExist:
            print('Some selected users do not exist')


        return HttpResponseRedirect(reverse('adminDashboard'))

    return HttpResponseRedirect(reverse('adminDashboard'))

def personEdit(request,rowId):
    person = Person.objects.all().values('id','name','dob','blood_group','licence_no')
    personSelected = Person.objects.filter(id=rowId).values('id', 'name', 'dob','blood_group','licence_no')
    columns = ["ID", "name", "dob",'blood_group','licence_no']
    popup = True

    return render(request,'displayPerson.html',{'person':person, 'columns':columns,'popup':popup,'editRow':personSelected})
    
def personSave(request):
    print(request)
    if request.method == 'POST':

        id = request.POST['id']
        name = request.POST['name']
        dob = request.POST['dob']
        blood_group = request.POST['blood_group']
        licence_no = request.POST['licence_no']

        try:

            user = Person.objects.get(id=id)

            user.name = name
            user.blood_group = blood_group
            user.licence_no = licence_no
            user.save()
            print('updated')
            return redirect('/adminDashboard/person/')
        except User.DoesNotExist:
            return redirect('/adminDashboard/')  
    return