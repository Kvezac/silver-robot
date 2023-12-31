from datetime import date, datetime

from django.core.validators import MinValueValidator
from django.db import models, transaction
from mptt.models import MPTTModel, TreeForeignKey

from user.models import Profile


class Position(models.Model):
    """
        Model Employee positions in a company
    """
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, blank=True)
    date_create = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'

    def __str__(self) -> str:
        return self.name


class Employee(MPTTModel):
    """
        The Employee model represents employees in a company.
    """

    name = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Имя сотрудника')
    position = models.ForeignKey('Position', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Должность')
    hire_date = models.DateField(default=datetime.now, blank=True, verbose_name='Дата принятия на работу')
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
                                 validators=[MinValueValidator(0)], verbose_name='Назначенная зарплата')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                            verbose_name='Руководитель')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        ordering = ['level']
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self) -> str:
        return f'{self.name.last_name}'

    def age(self) -> int:
        """
            Returns the number of years worked based on the hire date.
        """
        today = date.today()
        if self.hire_date:
            return today.year - self.hire_date.year - (
                    (today.month, today.day) < (self.hire_date.month, self.hire_date.day))
        else:
            return 0

    def get_parent(self) -> object:
        """
           Returns the employee's parent.
        """
        ancestors = self.get_ancestors()
        parent = ancestors.last()
        return parent if parent is not None else '-'

    def get_child_count(self) -> int:
        """
            Returns the number of descendants of the employee.
        """
        child_count = self.get_descendant_count()
        return child_count

    def get_descendant(self):
        """
            Returns all descendants of an employee.
        """
        descendant = self.get_descendants(include_self=True)
        return descendant

    def node_delete(self, *args, **kwargs):
        with transaction.atomic():
            super().delete(*args, **kwargs)
