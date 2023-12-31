import decimal
import os
import random
import string
from datetime import datetime

import django
from faker import Faker
from transliterate import translit

from company.management.decorators.clockdeco import clock

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from user.models import Profile
from company.models import Employee, Position
from django.contrib.auth.models import User

fake = Faker('ru-Ru')


@clock
def clear_table() -> None:
    for name_table in (Profile, User, Employee, Position):
        name_table.objects.all().delete()


@clock
def creat_position(total: int = 10) -> None:
    """
        Creates random vacancies and enters them into the database
    """
    for _ in range(total):
        vocation = Position()
        vocation.name = fake.unique.job()
        vocation.slug = last_name_translit(vocation.name).lower()
        vocation.save()


def creat_base(gender: str) -> tuple:
    """
        Creates a surname, first name, and patronymic depending on which gender is selected
    """
    if gender.lower() == 'female':
        last_name = fake.last_name_female()
        first_name = fake.first_name_female()
        middle_name = fake.middle_name_female()
        gender = 'Female'
    else:
        last_name = fake.last_name_male()
        first_name = fake.first_name_male()
        middle_name = fake.middle_name_male()
        gender = 'Male'
    return first_name, middle_name, last_name, gender


def year_limit(year_lim: int) -> tuple:
    """
       Calculates the limit by year from today's date
    """
    date_year = datetime.today().year - year_lim
    date_month = datetime.today().month
    date_day = datetime.today().day
    return date_year, date_month, date_day


def creat_gender() -> str:
    """
        Randomly selects gender from the list
    """
    list_gender = ['Female', 'Male']
    return random.choice(list_gender)


def creat_date_of_bth(min_year: int, max_year: int) -> object:
    """
      Generates a date of birth that fits the limit
    """
    current_year_young, current_month_young, current_day_young = year_limit(min_year)
    current_year_old, current_month_old, current_day_old = year_limit(max_year)
    creat_date = fake.date_between_dates(
        date_start=datetime(current_year_old, current_month_old, current_day_old),
        date_end=datetime(current_year_young, current_month_young, current_day_young))
    return creat_date


def last_name_translit(last_name: str) -> str:
    """
        Translates into English and removes gibberish upon receiving the translation
    """
    result = translit(last_name, 'ru', reversed=True).translate(str.maketrans('', '', string.punctuation))
    return result


def creat_email(last_name: str) -> str:
    """
        Creates email
    """
    return f'{last_name}_{fake.bothify(text="??####?")}@example.com'


def add_one(func):
    def inner(*args, **kwargs):
        """
            Add +1 for uniqueness username  in the table auth_user
        """
        inner.total += 1
        result = f'{func(*args, **kwargs)}{inner.total}'
        return result

    inner.total = 0
    return inner


@add_one
def creat_username(last_name: str) -> str:
    """
        Creates last name profile
    """
    result = f'{last_name}_'
    return result


def creat_phone() -> str:
    """
        Creates phone number
    """
    return f'+7{fake.bothify(text="#" * 10)}'


def creat_city() -> str:
    """
        creates city
    """
    return fake.city()


def creat_user(last_name) -> object:
    """
        Creates a basic login user with a fixed password
    """
    last_name_tr = last_name_translit(last_name)
    user = User.objects.create_user(
        username=creat_username(last_name_tr),
        email=creat_email(last_name_tr),
        password='1111')  # Qwer1234')
    return user


def update_profile() -> object:
    """
       Updates the created profile with the generated data
    """
    name, middle_name, last_name, gender = creat_base(creat_gender())
    user = creat_user(last_name)
    profile = Profile.objects.get(user_id=user.id)
    profile.name = name
    profile.middle_name = middle_name
    profile.last_name = last_name
    profile.gender = gender
    profile.date_of_bth = creat_date_of_bth(18, 65)
    profile.phone = creat_phone()
    profile.city = creat_city()
    profile.save()
    return profile


def creat_salary(min_salary: int, max_salary: int) -> decimal:
    """
        Create fake salary depending on what level the employee is
    """
    salary = fake.pydecimal(left_digits=5,
                            right_digits=2,
                            positive=True,
                            min_value=min_salary,
                            max_value=max_salary)

    return salary


def creat_employee(level: int, salary_lim: tuple = (10000, 20000)):
    """
        Creates an employee and writes it to the database.
        The boss is chosen randomly from the previous level.
        If there is no previous level, then there will be no leader
    """
    employee = Employee()
    employee.name = update_profile()
    employee.position = Position.objects.order_by("?").first()
    employee.hire_date = creat_date_of_bth(0, 10)
    employee.salary = creat_salary(*salary_lim)
    employee.parent = Employee.objects.filter(level=level - 1).order_by('?').first()
    employee.save()
