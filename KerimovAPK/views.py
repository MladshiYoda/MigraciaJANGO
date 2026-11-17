from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Airline, Airport, Flight, Passenger, Ticket
from .forms import AirlineForm, AirportForm, FlightForm, PassengerForm, TicketForm

# ================= Авиакомпании =================
class AirlineListView(ListView):
    model = Airline
    template_name = 'airline_list.html'

class AirlineDetailView(DetailView):
    model = Airline
    template_name = 'airline_detail.html'

class AirlineCreateView(CreateView):
    model = Airline
    form_class = AirlineForm
    template_name = 'airline_form.html'
    success_url = reverse_lazy('airline_list')

class AirlineUpdateView(UpdateView):
    model = Airline
    form_class = AirlineForm
    template_name = 'airline_form.html'
    success_url = reverse_lazy('airline_list')

class AirlineDeleteView(DeleteView):
    model = Airline
    template_name = 'airline_confirm_delete.html'
    success_url = reverse_lazy('airline_list')

# ================= Аэропорты =================
class AirportListView(ListView):
    model = Airport
    template_name = 'airport_list.html'

class AirportDetailView(DetailView):
    model = Airport
    template_name = 'airport_detail.html'

class AirportCreateView(CreateView):
    model = Airport
    form_class = AirportForm
    template_name = 'airport_form.html'
    success_url = reverse_lazy('airport_list')

class AirportUpdateView(UpdateView):
    model = Airport
    form_class = AirportForm
    template_name = 'airport_form.html'
    success_url = reverse_lazy('airport_list')

class AirportDeleteView(DeleteView):
    model = Airport
    template_name = 'airport_confirm_delete.html'
    success_url = reverse_lazy('airport_list')

# ================= Рейсы =================
class FlightListView(ListView):
    model = Flight
    template_name = 'flight_list.html'

class FlightDetailView(DetailView):
    model = Flight
    template_name = 'flight_detail.html'

class FlightCreateView(CreateView):
    model = Flight
    form_class = FlightForm
    template_name = 'flight_form.html'
    success_url = reverse_lazy('flight_list')

class FlightUpdateView(UpdateView):
    model = Flight
    form_class = FlightForm
    template_name = 'flight_form.html'
    success_url = reverse_lazy('flight_list')

class FlightDeleteView(DeleteView):
    model = Flight
    template_name = 'flight_confirm_delete.html'
    success_url = reverse_lazy('flight_list')

# ================= Пассажиры =================
class PassengerListView(ListView):
    model = Passenger
    template_name = 'passenger_list.html'

class PassengerDetailView(DetailView):
    model = Passenger
    template_name = 'passenger_detail.html'

class PassengerCreateView(CreateView):
    model = Passenger
    form_class = PassengerForm
    template_name = 'passenger_form.html'
    success_url = reverse_lazy('passenger_list')

class PassengerUpdateView(UpdateView):
    model = Passenger
    form_class = PassengerForm
    template_name = 'passenger_form.html'
    success_url = reverse_lazy('passenger_list')

class PassengerDeleteView(DeleteView):
    model = Passenger
    template_name = 'passenger_confirm_delete.html'
    success_url = reverse_lazy('passenger_list')

# ================= Билеты =================
class TicketListView(ListView):
    model = Ticket
    template_name = 'ticket_list.html'

class TicketDetailView(DetailView):
    model = Ticket
    template_name = 'ticket_detail.html'

class TicketCreateView(CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'ticket_form.html'
    success_url = reverse_lazy('ticket_list')

class TicketUpdateView(UpdateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'ticket_form.html'
    success_url = reverse_lazy('ticket_list')

class TicketDeleteView(DeleteView):
    model = Ticket
    template_name = 'ticket_confirm_delete.html'
    success_url = reverse_lazy('ticket_list')