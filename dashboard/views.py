from django.shortcuts import render,redirect
from adminDashboard.models import Vehicle

# Create your views here.

def dashboard(request):
    vehicle = Vehicle.objects.all().values('id','vehicle_no', 'engine_no', 'chassis_no','Fuel','Manufacturer')
    columns = ['vehicle_no', 'engine_no', 'chassis_no','Fuel','Manufacturer']
    print(vehicle)
    return render(request,'dashboard.html',{'vehicle':vehicle, 'columns':columns})

def track(request):
    return render(request,'track.html')

def adminDashboardRedirect(request):
    return redirect('adminDashboard')
