from django.test import TestCase

from datetime import date
from .models import Profile


class ProfileTestCase(TestCase):
    def setUp(self):
        self.profile = Profile.objects.create(
            last_name='Иванов',
            name='Иван',
            middle_name='Иванович',
            gender='Мужской',
            date_of_bth=date(1990, 5, 15),
            phone='+79396580017',
            city='Рязань'
        )

    def test_profile_age(self):
        self.assertEqual(self.profile.age(), 33)

    def test_profile_full_name(self):
        self.assertEqual(self.profile.full_name(), 'Иванов Иван Иванович')

    def test_profile_short_name(self):
        self.assertEqual(self.profile.short_name(), 'Иванов И.И.')

    def test_profile_str(self):
        self.assertEqual(str(self.profile), 'Иванов')

# Create your tests here.
