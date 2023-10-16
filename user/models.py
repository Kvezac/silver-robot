from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Мужской'),
        ('Female', 'Женский'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES, blank=True, null=True)
    date_of_bth = models.DateField(auto_now=False, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.__class__.__name__}: {self.last_name}'
