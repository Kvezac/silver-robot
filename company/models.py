from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from user.models import Profile


class Employee(MPTTModel):
    name = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    position = TreeForeignKey('Position', on_delete=models.PROTECT, null=True, blank=True)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255)
    date_create = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
