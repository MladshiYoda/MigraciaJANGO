from datetime import timedelta
from decimal import Decimal
from io import BytesIO
from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone
from .models import Airline, Airport, Aircraft, Flight, Passenger, Ticket, CrewMember, FlightCrew
from PIL import Image

class ApplicationTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.airline = Airline.objects.create(name='Тестовая авиакомпания')
        cls.airport1 = Airport.objects.create(name='Первый', city='Москва')
        cls.airport2 = Airport.objects.create(name='Второй', city='Казань')
        cls.aircraft = Aircraft.objects.create(model_name='Тестовый самолёт', capacity=180, airline=cls.airline)
        cls.flight = Flight.objects.create(flight_number='TEST1', departure=cls.airport1, arrival=cls.airport2, aircraft=cls.aircraft, departure_time=timezone.now()+timedelta(days=1))
        cls.passenger = Passenger.objects.create(first_name='Тест', last_name='Пассажир', passport='1234567890')
        cls.ticket = Ticket.objects.create(flight=cls.flight, passenger=cls.passenger, seat='2A', price=Decimal('4500.00'))
        cls.crew = CrewMember.objects.create(name='Тест Экипаж', role='Пилот', airline=cls.airline)
        cls.flightcrew = FlightCrew.objects.create(flight=cls.flight, crew_member=cls.crew)

    def test_navigation_routes(self):
        for name in ['home','about','contacts','directions','services','information']:
            with self.subTest(name=name):
                response=self.client.get(reverse(name))
                self.assertEqual(response.status_code,200)
                self.assertContains(response,'Аэропорт Керимов')

    def test_all_eight_crud_create_update_delete(self):
        items = [
            ('airline',Airline,{'name':'Новая компания'},{'name':'Изменённая компания'}),
            ('airport',Airport,{'name':'Третий','city':'Пермь'},{'name':'Новый терминал','city':'Пермь'}),
            ('aircraft',Aircraft,{'model_name':'A220','capacity':'140','airline':str(self.airline.pk)},{'model_name':'A221','capacity':'140','airline':str(self.airline.pk)}),
            ('flight',Flight,{'flight_number':'TST9','departure':str(self.airport1.pk),'arrival':str(self.airport2.pk),'aircraft':str(self.aircraft.pk),'departure_time':'2027-04-20T12:30'},{'flight_number':'TST8','departure':str(self.airport1.pk),'arrival':str(self.airport2.pk),'aircraft':str(self.aircraft.pk),'departure_time':'2027-04-21T12:30'}),
            ('passenger',Passenger,{'first_name':'Новый','last_name':'Пассажир','passport':'990011'},{'first_name':'Изменён','last_name':'Пассажир','passport':'990011'}),
            ('ticket',Ticket,{'flight':str(self.flight.pk),'passenger':str(self.passenger.pk),'seat':'4B','price':'1050.00'},{'flight':str(self.flight.pk),'passenger':str(self.passenger.pk),'seat':'4C','price':'1050.00'}),
            ('crewmember',CrewMember,{'name':'Новый пилот','role':'Пилот','airline':str(self.airline.pk)},{'name':'Новый пилот','role':'Штурман','airline':str(self.airline.pk)}),
            ('flightcrew',FlightCrew,{'flight':str(self.flight.pk),'crew_member':str(self.crew.pk)},{'flight':str(self.flight.pk),'crew_member':str(self.crew.pk)}),
        ]
        for slug, model, create_data, update_data in items:
            with self.subTest(entity=slug):
                initial=model.objects.count()
                self.assertEqual(self.client.get(reverse(slug+'_list')).status_code,200)
                response=self.client.get(reverse(slug+'_create'))
                self.assertEqual(response.status_code,200)
                response=self.client.post(reverse(slug+'_create'),create_data)
                self.assertRedirects(response,reverse(slug+'_list'))
                self.assertEqual(model.objects.count(),initial+1)
                obj=model.objects.order_by('-pk').first()
                self.assertEqual(self.client.get(reverse(slug+'_detail',args=[obj.pk])).status_code,200)
                response=self.client.post(reverse(slug+'_update',args=[obj.pk]),update_data)
                self.assertRedirects(response,reverse(slug+'_list'))
                self.assertEqual(self.client.get(reverse(slug+'_delete',args=[obj.pk])).status_code,200)
                response=self.client.post(reverse(slug+'_delete',args=[obj.pk]))
                self.assertRedirects(response,reverse(slug+'_list'))
                self.assertEqual(model.objects.count(),initial)

    def test_image_upload_on_two_tables(self):
        buffer=BytesIO()
        Image.new('RGB',(20,20),'blue').save(buffer,format='PNG')
        for slug, instance, field, data in [('airline',self.airline,'logo',{'name':'Авиакомпания с фото'}),('airport',self.airport1,'photo',{'name':'Аэропорт с фото','city':'Москва'})]:
            with self.subTest(slug=slug):
                f=SimpleUploadedFile('image.png',buffer.getvalue(),content_type='image/png')
                response=self.client.post(reverse(slug+'_update',args=[instance.pk]),{**data,field:f})
                self.assertRedirects(response,reverse(slug+'_list'))
                instance.refresh_from_db()
                self.assertTrue(bool(getattr(instance,field)))
                self.assertContains(self.client.get(reverse(slug+'_list')),'/media/')
