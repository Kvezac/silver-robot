from datetime import date

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Мужской'),
        ('Female', 'Женский'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Фамилия')
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Имя')
    middle_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Отчество')
    image = models.ImageField(upload_to='profiles/images', blank=True, null=True,
                              default='profiles/images/user-default.png')
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES, blank=True, null=True, verbose_name='Пол')
    date_of_bth = models.DateField(auto_now=False, blank=True, null=True, verbose_name='Дата Рождения')
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Номер Телефона')
    city = models.CharField(max_length=255, blank=True, null=True, verbose_name='Место Проживания')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self) -> str:
        return f'{self.last_name}'

    def age(self) -> int:
        today = date.today()
        if self.date_of_bth:
            return today.year - self.date_of_bth.year - (
                    (today.month, today.day) < (self.date_of_bth.month, self.date_of_bth.day))
        else:
            return 0

    def full_name(self) -> str:
        return f'{self.last_name} {self.name} {self.middle_name}'

    def short_name(self) -> str:
        if self.last_name:
            return f'{self.last_name} {self.name[0].upper()}.{self.middle_name[0].upper()}.'
        return ''
