from django.db import models

# 1. Авиакомпания (С ФОТО)
class Airline(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название авиакомпании')
    logo = models.ImageField(upload_to='airlines/', null=True, blank=True, verbose_name='Логотип')
    def __str__(self): return self.name

# 2. Аэропорт (С ФОТО)
class Airport(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название аэропорта')
    city = models.CharField(max_length=50, verbose_name='Город')
    photo = models.ImageField(upload_to='airports/', null=True, blank=True, verbose_name='Фото аэропорта')
    def __str__(self): return f"{self.name} ({self.city})"

# 3. Самолет
class Aircraft(models.Model):
    model_name = models.CharField(max_length=50, verbose_name='Модель самолета')
    capacity = models.IntegerField(verbose_name='Вместимость')
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, verbose_name='Авиакомпания')
    def __str__(self): return self.model_name

# 4. Рейс
class Flight(models.Model):
    flight_number = models.CharField(max_length=10, verbose_name='Номер рейса')
    departure = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures', verbose_name='Откуда')
    arrival = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals', verbose_name='Куда')
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE, verbose_name='Самолет')
    departure_time = models.DateTimeField(verbose_name='Время вылета')
    def __str__(self): return f"{self.flight_number}: {self.departure.city} - {self.arrival.city}"

# 5. Пассажир
class Passenger(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    passport = models.CharField(max_length=20, verbose_name='Паспорт')
    def __str__(self): return f"{self.first_name} {self.last_name}"

# 6. Билет
class Ticket(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, verbose_name='Рейс')
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, verbose_name='Пассажир')
    seat = models.CharField(max_length=5, verbose_name='Место')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    def __str__(self): return f"Билет {self.seat} на {self.flight.flight_number}"

# 7. Член экипажа
class CrewMember(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя сотрудника')
    role = models.CharField(max_length=50, verbose_name='Должность')
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, verbose_name='Авиакомпания')
    def __str__(self): return self.name

# 8. Назначение на рейс
class FlightCrew(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, verbose_name='Рейс')
    crew_member = models.ForeignKey(CrewMember, on_delete=models.CASCADE, verbose_name='Сотрудник')
    def __str__(self): return f"{self.crew_member.name} на {self.flight.flight_number}"