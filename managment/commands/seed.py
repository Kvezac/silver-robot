import random
from datetime import datetime

from faker import Faker
from transliterate import translit

from user.models import Profile
from company.models import Employee, Position
from django.contrib.auth.models import User

fake = Faker('ru-Ru')
fake.seed(4321)


def creat_position(total: int = 10) -> None:
    for _ in range(total):
        vocation = Position()
        vocation.name = fake.unique.job()
        vocation.slug = last_name_translit(vocation.name).lower()
        Position.objects.create(vocation)


def creat_base(gender: str) -> tuple:
    if gender == 'female':
        last_name = fake.last_name_female()
        first_name = fake.first_name_female()
        middle_name = fake.middle_name_female()
        gender = 'Женский'
    else:
        last_name = fake.last_name_male()
        first_name = fake.first_name_male()
        middle_name = fake.middle_name_male()
        gender = 'Мужской'
    return first_name, middle_name, last_name, gender


def year_limit(year_lim: int) -> tuple:
    date_year = datetime.today().year - year_lim
    date_month = datetime.today().month
    date_day = datetime.today().day
    return date_year, date_month, date_day


def creat_gender():
    list_gender = ['female', 'male']
    return random.choice(list_gender)


def year_limit(year_lim: int) -> tuple:
    date_year = datetime.today().year - year_lim
    date_month = datetime.today().month
    date_day = datetime.today().day
    return date_year, date_month, date_day


def creat_date_of_bth(min_year: int, max_year: int) -> object:
    current_year_young, current_month_young, current_day_young = year_limit(min_year)
    current_year_old, current_month_old, current_day_old = year_limit(max_year)
    creat_date = fake.date_between_dates(
        date_start=datetime(current_year_old, current_month_old, current_day_old),
        date_end=datetime(current_year_young, current_month_young, current_day_young))
    return creat_date


def last_name_translit(last_name: str) -> str:
    return translit(last_name, 'ru', reversed=True)


def creat_email(last_name: str) -> str:
    return f'{last_name[:5]}_{fake.bothify(text="??####")}@example.com'


def creat_phone() -> str:
    return f'+7{fake.bothify(text="#" * 10)}'


def creat_city() -> str:
    return fake.city()


def creat_user(last_name):
    last_name_tr = last_name_translit(last_name)

    user = User.objects.create_user(
        username=last_name_tr,
        email=creat_email(last_name_tr),
        password='Qwer1234')
    user.save()
    return user


def create_profile() -> object:
    profile = Profile()
    profile.name, \
        profile.middle_name, \
        profile.last_name, \
        profile.gender = creat_base(creat_gender())
    profile.date_of_bth = creat_date_of_bth(18, 65)
    profile.phone = creat_phone()
    profile.city = creat_city()
    profile.user = creat_user(profile.last_name)
    profile.save()
    return profile


def creat_salary(min_salary, max_salary) -> str:
    salary = fake.pydecimal(left_digits=5,
                            right_digits=2,
                            positive=True,
                            min_value=min_salary,
                            max_value=max_salary)

    return salary


def creat_employee():
    employee = Employee()
    employee.name = create_profile()
    employee.position = Position.objects.order_by("?").first()
    employee.hire_date = creat_date_of_bth(0, 10)
    employee.salary = creat_salary(50000, 100000)
    employee.parent = Employee.objects.filter(gi).order_by('?').first()
    Employee.objects.create(employee)
    employee.save()


if __name__ == '__main__':
    print(creat_position(10))
