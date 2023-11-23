## Проект для генерации данных. Реализован на базе предполагаемого предприятия в котором есть руководители и подчиненные. 
## Также в самом проекте реализована:
* регистрация
* просмотр профиля
* редактирование профиля
* удаление

### Технологии:
* python
* HTML
* CSS
* JS
* Bootstrap



##  Для установки:

* Клонировать репозиторий на локальный компьютер
```commandline
git clone https://github.com/Kvezac/silver-robot.git
```
* Установить зависимости
```commandline
pip install -r requirements.txt
```
* Создать миграции на основе моделей
```commandline
python manage.py makemigrations
```
* Выполнить миграции
```commandline
python manage.py migrate
```
* Заполнить базу данных командой из терминала.  
Команда имеет два позиционных аргумента:
- Количество профессий 'position' default=20.
- Количество сотрудников 'total_employee' default=500.  
  
Пример с аргументами:
```commandline
python manage.py seed 200 50000
```
Пример без аргументов:
```commandline
python manage.py seed
```
* Заполнить базу профилями не являющимися сотрудниками.
Команда имеет один позиционный аргумент:
- Количество профилей 'total_profile' default=20

Пример с аргументами.
```commandline
python manage.py seed_user 50
```
Пример без аргументов:
```commandline
python manage.py seed_user
```
Запуск проекта:
```commandline
python manage.py runserver
```