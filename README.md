## Проект "Онлайн каталог сотрудников компании" представляет собой веб-приложение, предназначенное для хранения информации о сотрудниках компании и их иерархии.

## Проект разработан для удобного хранения и управления информацией о сотрудниках компании и может быть доработан в соответствии с потребностями компании

## План проекта:

1. Создать базу данных для хранения информации о сотрудниках.
2. Разработать веб страницу для вывода иерархии сотрудников в древовидной форме.
3. Добавить информацию о каждом сотруднике в базу данных, включая ФИО, должность, дату приема на работу и размер
   заработной платы.
4. Установить связь между каждым сотрудником и его начальником.
5. Заполнить базу данных не менее чем 50 000 сотрудниками и 5 уровнями иерархии.
6. Отобразить должность каждого сотрудника на веб странице.
7. Создать базу данных с помощью миграций Django.
8. Использовать DB seeder для заполнения базы данных.
9. Использовать Twitter Bootstrap для создания базовых стилей веб страницы.
10. Создать страницу со списком всех сотрудников и отображением всей имеющейся информации из базы данных, а также
    возможностью сортировки по любому полю.
11. Добавить возможность поиска сотрудников по любому полю на странице.
12. Добавить возможность сортировки и поиска по любому полю без перезагрузки страницы с
    помощью ajax.
13. Осуществить аутентификацию пользователя для доступа к разделу веб сайта, доступному только для зарегистрированных
    пользователей, с использованием стандартных функций Django.
14. Перенести функционал из пунктов №10, №11 и №12 (с использованием ajax запросов) в раздел доступный только для
    зарегистрированных пользователей.
15. Реализовать CRUD операции для записей сотрудников в разделе доступном только для зарегистрированных пользователей,
    включая возможность редактирования всех полей, включая начальника каждого сотрудника.
16. Добавить возможность загружать фотографию сотрудника и отображать ее на странице редактирования данных о сотруднике,
    а также добавить дополнительную колонку с уменьшенной фотографией на страницу списка всех сотрудников.
17. Реализовать возможность перераспределения сотрудников при изменении начальника с помощью встроенных
    механизмов/парадигм, предлагаемых Django ORM.
18. Реализовать ленивую загрузку для дерева сотрудников, показывая первые два уровня иерархии по умолчанию и подгружая 2
    следующих уровня или всю ветку дерева при клике на сотрудника второго уровня.
19. Реализовать возможность изменения начальника сотрудника с помощью drag-n-drop в дереве сотрудников.
20. Добавить возможность экспорта списка сотрудников в формате CSV или Excel.
21. Реализовать функционал уведомлений для изменения данных о сотрудниках, отправляя уведомления на email начальника и
    администратора системы.
22. Добавить возможность просмотра истории изменений данных о сотруднике.
23. Реализовать систему прав доступа, позволяющую ограничивать доступ к разделам и функционалу в зависимости от роли
    пользователя.
24. Создать страницу отчетов, позволяющую генерировать отчеты по различным параметрам, например, количество сотрудников
    в каждом отделе или общая зарплата по отделам.
25. Реализовать функционал подтверждения удаления записей о сотрудниках.
26. Добавить возможность загрузки документов (например, резюме или контракта) на страницу редактирования данных о
    сотруднике.