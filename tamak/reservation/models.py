from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import reverse



class Reservation(models.Model):
    AMOUNT_OF_PERSONS = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
    )
    
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_phone = models.CharField(max_length=25, verbose_name="Номер Телефона:")
    date_of_reservation = models.DateField(verbose_name="Дата Бронирования:")
    time_of_reservation = models.TimeField(verbose_name="Время Бронирования:")
    persons = models.CharField(choices=AMOUNT_OF_PERSONS, default=AMOUNT_OF_PERSONS[0][0], max_length=8, verbose_name="Количество человек:")
    comment = models.TextField(verbose_name="Комментарий:")

    def __str__(self) -> str:
        return self.client.first_name + ' ' + self.client.last_name

