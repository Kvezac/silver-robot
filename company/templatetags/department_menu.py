from django import template

from company.models import Employee

register = template.Library()


@register.inclusion_tag('tags/departament_menu.html', takes_context=True)
def departament_menu(context):
    employees = Employee.objects.all()
    levels = set([employee.get_level() for employee in employees])
    result = {'levels': levels}
    return result
