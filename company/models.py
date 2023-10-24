from datetime import date

from django.db import models, connection
from mptt.models import MPTTModel, TreeForeignKey
from user.models import Profile


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, blank=True)
    date_create = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'

    def __str__(self) -> str:
        return self.name

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table}')


class Employee(MPTTModel):
    name = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    position = models.ForeignKey('Position', on_delete=models.PROTECT, null=True, blank=True)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['salary']

    class Meta:
        ordering = ['level']
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self) -> str:
        return f'{self.__class__.__name__}: {self.pk} {self.name.last_name}'

    def age(self) -> int:
        today = date.today()
        if self.hire_date:
            return today.year - self.hire_date.year - (
                        (today.month, today.day) < (self.hire_date.month, self.hire_date.day))
        else:
            return 0
