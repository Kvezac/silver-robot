# import random
# from datetime import datetime
# # import re
#
# from faker import Faker
#
#
# def creat_base(fake, gender_choice, ):
#     """ Генерация Фамилии Имя пол в зависимости от переданного параметра"""
#     if gender_choice == 'female':
#         last_name = fake.last_name_female()
#         first_name = fake.first_name_female()
#         gen = 'жен'
#     else:
#         last_name = fake.last_name_male()
#         first_name = fake.first_name_male()
#         gen = 'муж'
#     return last_name, first_name, gen
#
#
# def year_limit(year_lim):
#     """ Установление лимита по возрасту от 18 до 65
#     """
#     date_year = datetime.today().year - year_lim
#     date_month = datetime.today().month
#     date_day = datetime.today().day
#     return date_year, date_month, date_day
#
#
# creat_list = []
#
#
# def creat_base_employees():
#     """ Создание базы данных сотрудников и запись построчно в базу данных.
#         Данные для записи:
#             Фамилия
#             Имя
#             Дата рождения
#             Полных лет
#             пол (муж, жен)
#     """

# for _ in range(int(input("Введите количество сотрудников\n: "))):
#     """"Количество сотрудников ограниченных пользователем"""
#     gender = random.choice(['female', 'male'])
#     employee = Faker('ru_Ru')
#     creat_last, creat_first, gen = creat_base(employee, gender)
#     current_year_young, current_month_young, current_day_young = year_limit(18)
#     current_year_old, current_month_old, current_day_old = year_limit(65)
#     date_birth = employee.date_between_dates(
#         date_start=datetime(current_year_old, current_month_old, current_day_old),
#         date_end=datetime(current_year_young, current_month_young, current_day_young))
#     year = datetime.today().year - date_birth.year
#     # date_obj = re.sub(r'(\d{4})(\-)(\d{2})\2(\d{2})', r'\4.\3.\1', str(date_birth))
#     creat_list.append(f'{creat_last} {creat_first} {year} {gen}')
# return creat_list


