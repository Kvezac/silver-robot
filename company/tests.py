from django.test import TestCase
from datetime import date
from .models import Position, Employee
from user.models import Profile


class EmployeeTestCase(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name='Менеджер', slug='manager')
        self.profile = Profile.objects.create(name='Иванов', last_name='Иван')
        self.employee = Employee.objects.create(name=self.profile, position=self.position, hire_date=date(2020, 1, 1),
                                                salary=50000)

    def test_employee_age(self):
        self.assertEqual(self.employee.age(), 3)

    # def test_employee_parent(self):
    #     self.assertIsNone(self.employee.get_parent(), 'Иванов')

    def test_employee_child_count(self):
        self.assertEqual(self.employee.get_child_count(), 0)

    def test_position_str(self):
        self.assertEqual(str(self.position), 'Менеджер')

    def test_employee_str(self):
        self.assertEqual(str(self.employee), 'Иван')

    def test_position_verbose_name(self):
        self.assertEqual(Position._meta.verbose_name, 'Профессия')

    def test_employee_verbose_name(self):
        self.assertEqual(Employee._meta.verbose_name, 'Сотрудник')

    def test_position_plural_name(self):
        self.assertEqual(Position._meta.verbose_name_plural, 'Профессии')

    def test_employee_plural_name(self):
        self.assertEqual(Employee._meta.verbose_name_plural, 'Сотрудники')
