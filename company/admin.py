from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
# from mptt.admin import MPTTModelAdmin
from .models import Position, Employee


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    readonly_fields = ("slug", "date_create")


@admin.register(Employee)
class EmployeeAdmin(DjangoMpttAdmin):
    list_display = ('name', 'position', 'salary',)

