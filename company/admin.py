from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
# from mptt.admin import MPTTModelAdmin
from .models import Position, Employee


# @admin.register(Position)
# class PositionAdmin(admin.ModelAdmin):
#     readonly_fields = ("slug", "date_create")
#
#
# @admin.register(Employee)
# class EmployeeAdmin(DjangoMpttAdmin):
#     pass


class PositionAdmin(admin.ModelAdmin):
    model = Employee
    extra = 5


class EmployeeAdmin(DjangoMpttAdmin):
    list_display = ['name', 'position', 'salary', 'hide_date']


admin.site.register(Position)
admin.site.register(Employee)
