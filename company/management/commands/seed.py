from django.core.management import BaseCommand

from company.management.commands._tools import creat_position, creat_employee, clear_table
from company.management.decorators.clockdeco import clock


class Command(BaseCommand):
    """
        The team fills the employee database with the generated data.
    """
    help = 'Заполняет базу сотрудников сгенерированными данными'

    def add_arguments(self, parser):
        parser.add_argument('position', type=int, nargs='?', default=20,
                            help='Количество создаваемых должностей')
        parser.add_argument('total_employee', type=int, nargs='?', default=50,
                            help='Количество создаваемых сотрудников')

    @clock
    def handle(self, *args, **kwargs):
        """
        Runs commands:
         clear_table() clearing tables, does not reset the id counter
         creat_position() creates random positions with a given default quantity 20
         creat_employee() creates employees by levels with a given number default quantity 500
        """
        clear_table()
        position = kwargs['position']
        total_employee = kwargs['total_employee']

        first_employee = [1, (80000, 100000)]
        department_1 = [int((total_employee / 100 * 3)), (50000, 70000)]
        department_2 = [int((total_employee / 100 * 7)), (40000, 55000)]
        department_3 = [int((total_employee / 100 * 30)), (30000, 45000)]
        department_4 = [int((total_employee / 100 * 60) - 1), (20000, 35000)]
        all_employees = [first_employee, department_1, department_2, department_3, department_4]
        creat_position(position)
        for level, i in enumerate(all_employees, 0):
            for j in range(i[0]):
                creat_employee(level, i[1])


