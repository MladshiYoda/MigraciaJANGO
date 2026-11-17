from django.contrib import admin
from .models import *

admin.site.register(Airline)
admin.site.register(Airport)
admin.site.register(Aircraft)
admin.site.register(Flight)
admin.site.register(Passenger)
admin.site.register(Ticket)
admin.site.register(CrewMember)
admin.site.register(FlightCrew)