from django import forms
from .models import Group, Vehicle, Device, Person
from django.contrib.auth.models import User

class GroupForm(forms.ModelForm):
    # Define choices for the vehicleId field
    vehicle_choices = [(vehicle.id, vehicle.__int__()) for vehicle in Vehicle.objects.all()]

    vehicleId = forms.ChoiceField(
        choices=vehicle_choices,
        widget=forms.Select(attrs={'class': 'select2'}),
    )

    # Define choices for the deviceId field
    device_choices = [(device.id, device.__int__()) for device in Device.objects.all()]

    deviceId = forms.ChoiceField(
        choices=device_choices,
        widget=forms.Select(attrs={'class': 'select2'}),
    )

    # Define choices for the personId field
    person_choices = [(person.id, person.__str__()) for person in Person.objects.all()]

    personId = forms.ChoiceField(
        choices=person_choices,
        widget=forms.Select(attrs={'class': 'select2'}),
    )

    user_choices = [(user.id, user.username) for user in User.objects.all()]

    userId = forms.ChoiceField(
        choices=user_choices,
        widget=forms.Select(attrs={'class': 'select2'}),
    )
    
    class Meta:
        model = Group
        fields = ['name', 'vehicleId', 'deviceId', 'personId', 'userId']