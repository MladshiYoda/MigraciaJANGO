from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.contrib import messages
from . import models, forms

class HomeView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_flights'] = models.Flight.objects.select_related('departure', 'arrival', 'aircraft').order_by('departure_time')[:6]
        context['flights_count'] = models.Flight.objects.count()
        context['airports_count'] = models.Airport.objects.count()
        context['passengers_count'] = models.Passenger.objects.count()
        return context

class AboutView(TemplateView): template_name = 'about.html'
class ContactsView(TemplateView): template_name = 'contacts.html'
class DirectionsView(TemplateView): template_name = 'directions.html'
class ServicesView(TemplateView): template_name = 'page1.html'
class InformationView(TemplateView): template_name = 'page2.html'

# Авиакомпании
class AirlineListView(ListView):
    model = models.Airline
    template_name = 'crud_list.html'
    extra_context = {'entity_title': 'Авиакомпании', 'entity_single': 'Авиакомпания', 'entity_key': 'airline'}

class AirlineDetailView(DetailView):
    model = models.Airline
    template_name = 'crud_detail.html'
    extra_context = {'entity_title': 'Авиакомпании', 'entity_single': 'Авиакомпания', 'entity_key': 'airline'}

class AirlineCreateView(SuccessMessageMixin, CreateView):
    model = models.Airline
    form_class = forms.AirlineForm
    template_name = 'crud_form.html'
    success_url = reverse_lazy('airline_list')
    success_message = 'Запись успешно добавлена.'
    extra_context = {'entity_title': 'Авиакомпании', 'entity_single': 'Авиакомпания', 'entity_key': 'airline'}

class AirlineUpdateView(SuccessMessageMixin, UpdateView):
    model = models.Airline
    form_class = forms.AirlineForm
    template_name = 'crud_form.html'
    success_url = reverse_lazy('airline_list')
    success_message = 'Изменения сохранены.'
    extra_context = {'entity_title': 'Авиакомпании', 'entity_single': 'Авиакомпания', 'entity_key': 'airline'}

class AirlineDeleteView(DeleteView):
    model = models.Airline
    template_name = 'crud_confirm_delete.html'
    success_url = reverse_lazy('airline_list')
    extra_context = {'entity_title': 'Авиакомпании', 'entity_single': 'Авиакомпания', 'entity_key': 'airline'}
    def form_valid(self, form):
        messages.success(self.request, 'Запись удалена.')
        return super().form_valid(form)

# Аэропорты
class AirportListView(ListView):
    model = models.Airport
    template_name = 'crud_list.html'
    extra_context = {'entity_title': 'Аэропорты', 'entity_single': 'Аэропорт', 'entity_key': 'airport'}

class AirportDetailView(DetailView):
    model = models.Airport
    template_name = 'crud_detail.html'
    extra_context = {'entity_title': 'Аэропорты', 'entity_single': 'Аэропорт', 'entity_key': 'airport'}

class AirportCreateView(SuccessMessageMixin, CreateView):
    model = models.Airport
    form_class = forms.AirportForm
    template_name = 'crud_form.html'
    success_url = reverse_lazy('airport_list')
    success_message = 'Запись успешно добавлена.'
    extra_context = {'entity_title': 'Аэропорты', 'entity_single': 'Аэропорт', 'entity_key': 'airport'}

class AirportUpdateView(SuccessMessageMixin, UpdateView):
    model = models.Airport
    form_class = forms.AirportForm
    template_name = 'crud_form.html'
    success_url = reverse_lazy('airport_list')
    success_message = 'Изменения сохранены.'
    extra_context = {'entity_title': 'Аэропорты', 'entity_single': 'Аэропорт', 'entity_key': 'airport'}

class AirportDeleteView(DeleteView):
    model = models.Airport
    template_name = 'crud_confirm_delete.html'
    success_url = reverse_lazy('airport_list')
    extra_context = {'entity_title': 'Аэропорты', 'entity_single': 'Аэропорт', 'entity_key': 'airport'}
    def form_valid(self, form):
        messages.success(self.request, 'Запись удалена.')
        return super().form_valid(form)

# Самолёты
class AircraftListView(ListView):
    model = models.Aircraft
    template_name = 'crud_list.html'
    extra_context = {'entity_title': 'Самолёты', 'entity_single': 'Самолёт', 'entity_key': 'aircraft'}

class AircraftDetailView(DetailView):
    model = models.Aircraft
    template_name = 'crud_detail.html'
    extra_context = {'entity_title': 'Самолёты', 'entity_single': 'Самолёт', 'entity_key': 'aircraft'}

class AircraftCreateView(SuccessMessageMixin, CreateView):
    model = models.Aircraft
    form_class = forms.AircraftForm
    template_name = 'crud_form.html'
    success_url = reverse_lazy('aircraft_list')
    success_message = 'Запись успешно добавлена.'
    extra_context = {'entity_title': 'Самолёты', 'entity_single': 'Самолёт', 'entity_key': 'aircraft'}

class AircraftUpdateView(SuccessMessageMixin, UpdateView):
    model = models.Aircraft
    form_class = forms.AircraftForm
    template_name = 'crud_form.html'
    success_url = reverse_lazy('aircraft_list')
    success_message = 'Изменения сохранены.'
    extra_context = {'entity_title': 'Самолёты', 'entity_single': 'Самолёт', 'entity_key': 'aircraft'}

class AircraftDeleteView(DeleteView):
    model = models.Aircraft
    template_name = 'crud_confirm_delete.html'
    success_url = reverse_lazy('aircraft_list')
    extra_context = {'entity_title': 'Самолёты', 'entity_single': 'Самолёт', 'entity_key': 'aircraft'}
    def form_valid(self, form):
        messages.success(self.request, 'Запись удалена.')
        return super().form_valid(form)

# Рейсы
class FlightListView(ListView):
    model = models.Flight
    template_name = 'crud_list.html'
    extra_context = {'entity_title': 'Рейсы', 'entity_single': 'Рейс', 'entity_key': 'flight'}

class FlightDetailView(DetailView):
    model = models.Flight
    template_name = 'crud_detail.html'
    extra_context = {'entity_title': 'Рейсы', 'entity_single': 'Рейс', 'entity_key': 'flight'}

class FlightCreateView(SuccessMessageMixin, CreateView):
    model = models.Flight
    form_class = forms.FlightForm
    template_name = 'crud_form.html'
    success_url = reverse_lazy('flight_list')
    success_message = 'Запись успешно добавлена.'
    extra_context = {'entity_title': 'Рейсы', 'entity_single': 'Рейс', 'entity_key': 'flight'}

class FlightUpdateView(SuccessMessageMixin, UpdateView):
    model = models.Flight
    form_class = forms.FlightForm
    template_name = 'crud_form.html'
    success_url = reverse_lazy('flight_list')
    success_message = 'Изменения сохранены.'
    extra_context = {'entity_title': 'Рейсы', 'entity_single': 'Рейс', 'entity_key': 'flight'}

class FlightDeleteView(DeleteView):
    model = models.Flight
    template_name = 'crud_confirm_delete.html'
    success_url = reverse_lazy('flight_list')
    extra_context = {'entity_title': 'Рейсы', 'entity_single': 'Рейс', 'entity_key': 'flight'}
    def form_valid(self, form):
        messages.success(self.request, 'Запись удалена.')
        return super().form_valid(form)

# Пассажиры
class PassengerListView(ListView):
    model = models.Passenger
    template_name = 'crud_list.html'
    extra_context = {'entity_title': 'Пассажиры', 'entity_single': 'Пассажир', 'entity_key': 'passenger'}

class PassengerDetailView(DetailView):
    model = models.Passenger
    template_name = 'crud_detail.html'
    extra_context = {'entity_title': 'Пассажиры', 'entity_single': 'Пассажир', 'entity_key': 'passenger'}

class PassengerCreateView(SuccessMessageMixin, CreateView):
    model = models.Passenger
    form_class = forms.PassengerForm
    template_name = 'crud_form.html'
    success_url = reverse_lazy('passenger_list')
    success_message = 'Запись успешно добавлена.'
    extra_context = {'entity_title': 'Пассажиры', 'entity_single': 'Пассажир', 'entity_key': 'passenger'}

class PassengerUpdateView(SuccessMessageMixin, UpdateView):
    model = models.Passenger
    form_class = forms.PassengerForm
    template_name = 'crud_form.html'
    success_url = reverse_lazy('passenger_list')
    success_message = 'Изменения сохранены.'
    extra_context = {'entity_title': 'Пассажиры', 'entity_single': 'Пассажир', 'entity_key': 'passenger'}

class PassengerDeleteView(DeleteView):
    model = models.Passenger
    template_name = 'crud_confirm_delete.html'
    success_url = reverse_lazy('passenger_list')
    extra_context = {'entity_title': 'Пассажиры', 'entity_single': 'Пассажир', 'entity_key': 'passenger'}
    def form_valid(self, form):
        messages.success(self.request, 'Запись удалена.')
        return super().form_valid(form)

# Билеты
class TicketListView(ListView):
    model = models.Ticket
    template_name = 'crud_list.html'
    extra_context = {'entity_title': 'Билеты', 'entity_single': 'Билет', 'entity_key': 'ticket'}

class TicketDetailView(DetailView):
    model = models.Ticket
    template_name = 'crud_detail.html'
    extra_context = {'entity_title': 'Билеты', 'entity_single': 'Билет', 'entity_key': 'ticket'}

class TicketCreateView(SuccessMessageMixin, CreateView):
    model = models.Ticket
    form_class = forms.TicketForm
    template_name = 'crud_form.html'
    success_url = reverse_lazy('ticket_list')
    success_message = 'Запись успешно добавлена.'
    extra_context = {'entity_title': 'Билеты', 'entity_single': 'Билет', 'entity_key': 'ticket'}

class TicketUpdateView(SuccessMessageMixin, UpdateView):
    model = models.Ticket
    form_class = forms.TicketForm
    template_name = 'crud_form.html'
    success_url = reverse_lazy('ticket_list')
    success_message = 'Изменения сохранены.'
    extra_context = {'entity_title': 'Билеты', 'entity_single': 'Билет', 'entity_key': 'ticket'}

class TicketDeleteView(DeleteView):
    model = models.Ticket
    template_name = 'crud_confirm_delete.html'
    success_url = reverse_lazy('ticket_list')
    extra_context = {'entity_title': 'Билеты', 'entity_single': 'Билет', 'entity_key': 'ticket'}
    def form_valid(self, form):
        messages.success(self.request, 'Запись удалена.')
        return super().form_valid(form)

# Сотрудники экипажа
class CrewMemberListView(ListView):
    model = models.CrewMember
    template_name = 'crud_list.html'
    extra_context = {'entity_title': 'Сотрудники экипажа', 'entity_single': 'Сотрудник экипажа', 'entity_key': 'crewmember'}

class CrewMemberDetailView(DetailView):
    model = models.CrewMember
    template_name = 'crud_detail.html'
    extra_context = {'entity_title': 'Сотрудники экипажа', 'entity_single': 'Сотрудник экипажа', 'entity_key': 'crewmember'}

class CrewMemberCreateView(SuccessMessageMixin, CreateView):
    model = models.CrewMember
    form_class = forms.CrewMemberForm
    template_name = 'crud_form.html'
    success_url = reverse_lazy('crewmember_list')
    success_message = 'Запись успешно добавлена.'
    extra_context = {'entity_title': 'Сотрудники экипажа', 'entity_single': 'Сотрудник экипажа', 'entity_key': 'crewmember'}

class CrewMemberUpdateView(SuccessMessageMixin, UpdateView):
    model = models.CrewMember
    form_class = forms.CrewMemberForm
    template_name = 'crud_form.html'
    success_url = reverse_lazy('crewmember_list')
    success_message = 'Изменения сохранены.'
    extra_context = {'entity_title': 'Сотрудники экипажа', 'entity_single': 'Сотрудник экипажа', 'entity_key': 'crewmember'}

class CrewMemberDeleteView(DeleteView):
    model = models.CrewMember
    template_name = 'crud_confirm_delete.html'
    success_url = reverse_lazy('crewmember_list')
    extra_context = {'entity_title': 'Сотрудники экипажа', 'entity_single': 'Сотрудник экипажа', 'entity_key': 'crewmember'}
    def form_valid(self, form):
        messages.success(self.request, 'Запись удалена.')
        return super().form_valid(form)

# Назначения экипажа
class FlightCrewListView(ListView):
    model = models.FlightCrew
    template_name = 'crud_list.html'
    extra_context = {'entity_title': 'Назначения экипажа', 'entity_single': 'Назначение', 'entity_key': 'flightcrew'}

class FlightCrewDetailView(DetailView):
    model = models.FlightCrew
    template_name = 'crud_detail.html'
    extra_context = {'entity_title': 'Назначения экипажа', 'entity_single': 'Назначение', 'entity_key': 'flightcrew'}

class FlightCrewCreateView(SuccessMessageMixin, CreateView):
    model = models.FlightCrew
    form_class = forms.FlightCrewForm
    template_name = 'crud_form.html'
    success_url = reverse_lazy('flightcrew_list')
    success_message = 'Запись успешно добавлена.'
    extra_context = {'entity_title': 'Назначения экипажа', 'entity_single': 'Назначение', 'entity_key': 'flightcrew'}

class FlightCrewUpdateView(SuccessMessageMixin, UpdateView):
    model = models.FlightCrew
    form_class = forms.FlightCrewForm
    template_name = 'crud_form.html'
    success_url = reverse_lazy('flightcrew_list')
    success_message = 'Изменения сохранены.'
    extra_context = {'entity_title': 'Назначения экипажа', 'entity_single': 'Назначение', 'entity_key': 'flightcrew'}

class FlightCrewDeleteView(DeleteView):
    model = models.FlightCrew
    template_name = 'crud_confirm_delete.html'
    success_url = reverse_lazy('flightcrew_list')
    extra_context = {'entity_title': 'Назначения экипажа', 'entity_single': 'Назначение', 'entity_key': 'flightcrew'}
    def form_valid(self, form):
        messages.success(self.request, 'Запись удалена.')
        return super().form_valid(form)

