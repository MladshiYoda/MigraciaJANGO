from django import forms
from . import models

class AirlineForm(forms.ModelForm):
    class Meta:
        model = models.Airline
        fields = '__all__'

class AirportForm(forms.ModelForm):
    class Meta:
        model = models.Airport
        fields = '__all__'

class AircraftForm(forms.ModelForm):
    class Meta:
        model = models.Aircraft
        fields = '__all__'

class FlightForm(forms.ModelForm):
    class Meta:
        model = models.Flight
        fields = '__all__'
        widgets = {'departure_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['departure_time'].input_formats = ['%Y-%m-%dT%H:%M', '%Y-%m-%d %H:%M:%S']
        if self.instance and self.instance.pk and self.instance.departure_time:
            self.initial['departure_time'] = self.instance.departure_time.strftime('%Y-%m-%dT%H:%M')

class PassengerForm(forms.ModelForm):
    class Meta:
        model = models.Passenger
        fields = '__all__'

class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = '__all__'

class CrewMemberForm(forms.ModelForm):
    class Meta:
        model = models.CrewMember
        fields = '__all__'

class FlightCrewForm(forms.ModelForm):
    class Meta:
        model = models.FlightCrew
        fields = '__all__'

