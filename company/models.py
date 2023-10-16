from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from user.models import Profile


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, blank=True)
    # employee = TreeForeignKey('Employee', on_delete=models.PROTECT, blank=True)
    date_create = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'

    def __str__(self):
        return self.name


class Employee(MPTTModel):
    name = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    position = TreeForeignKey('Position', on_delete=models.PROTECT, null=True, blank=True)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        ordering = ['level']
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.__class__.__name__}: {self.pk} {self.name.last_name}'
