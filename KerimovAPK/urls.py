from django.urls import path
from . import views

urlpatterns = [
    # Авиакомпании
    path('airlines/', views.AirlineListView.as_view(), name='airline_list'),
    path('airlines/<int:pk>/', views.AirlineDetailView.as_view(), name='airline_detail'),
    path('airlines/create/', views.AirlineCreateView.as_view(), name='airline_create'),
    path('airlines/<int:pk>/update/', views.AirlineUpdateView.as_view(), name='airline_update'),
    path('airlines/<int:pk>/delete/', views.AirlineDeleteView.as_view(), name='airline_delete'),

    # Аэропорты
    path('airports/', views.AirportListView.as_view(), name='airport_list'),
    path('airports/<int:pk>/', views.AirportDetailView.as_view(), name='airport_detail'),
    path('airports/create/', views.AirportCreateView.as_view(), name='airport_create'),
    path('airports/<int:pk>/update/', views.AirportUpdateView.as_view(), name='airport_update'),
    path('airports/<int:pk>/delete/', views.AirportDeleteView.as_view(), name='airport_delete'),

    # Рейсы
    path('flights/', views.FlightListView.as_view(), name='flight_list'),
    path('flights/<int:pk>/', views.FlightDetailView.as_view(), name='flight_detail'),
    path('flights/create/', views.FlightCreateView.as_view(), name='flight_create'),
    path('flights/<int:pk>/update/', views.FlightUpdateView.as_view(), name='flight_update'),
    path('flights/<int:pk>/delete/', views.FlightDeleteView.as_view(), name='flight_delete'),

    # Пассажиры
    path('passengers/', views.PassengerListView.as_view(), name='passenger_list'),
    path('passengers/<int:pk>/', views.PassengerDetailView.as_view(), name='passenger_detail'),
    path('passengers/create/', views.PassengerCreateView.as_view(), name='passenger_create'),
    path('passengers/<int:pk>/update/', views.PassengerUpdateView.as_view(), name='passenger_update'),
    path('passengers/<int:pk>/delete/', views.PassengerDeleteView.as_view(), name='passenger_delete'),

    # Билеты
    path('tickets/', views.TicketListView.as_view(), name='ticket_list'),
    path('tickets/<int:pk>/', views.TicketDetailView.as_view(), name='ticket_detail'),
    path('tickets/create/', views.TicketCreateView.as_view(), name='ticket_create'),
    path('tickets/<int:pk>/update/', views.TicketUpdateView.as_view(), name='ticket_update'),
    path('tickets/<int:pk>/delete/', views.TicketDeleteView.as_view(), name='ticket_delete'),
]