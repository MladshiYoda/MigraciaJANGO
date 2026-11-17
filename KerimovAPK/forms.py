from django import forms
from .models import Airline, Airport, Flight, Passenger, Ticket

class AirlineForm(forms.ModelForm):
    class Meta:
        model = Airline
        fields = ['name', 'logo']

class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = ['name', 'city', 'photo']

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['flight_number', 'departure', 'arrival', 'aircraft', 'departure_time']

class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ['first_name', 'last_name', 'passport']

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['flight', 'passenger', 'seat', 'price']