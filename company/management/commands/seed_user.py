from django.core.management import BaseCommand

from company.management.commands._tools import update_profile
from company.management.decorators.clockdeco import clock


class Command(BaseCommand):
    """
        Creates employees without reference to position or position in the company.
    """
    help = 'Создаёт сотрудников без привязки к должности и позиции в компании'

    def add_arguments(self, parser):
        """
            Gets the number of profiles and creates them
        """
        parser.add_argument('total_profile', type=int, nargs='?', default=20,
                            help='Количество создаваемых пользователей')

    @clock
    def handle(self, *args, **kwargs):
        total_profile = kwargs['total_profile']

        for _ in range(total_profile):
            update_profile()
