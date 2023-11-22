from django import forms
from django.core.validators import MinValueValidator

from company.models import Employee, Position


class AddEmployeeForm(forms.ModelForm):
    parent = forms.ModelChoiceField(queryset=Employee.objects.all(), label='Начальник')
    position = forms.ModelChoiceField(queryset=Position.objects.all(), label='Position')
    salary = forms.DecimalField(label='Salary', validators=[MinValueValidator(0)])

    class Meta:
        model = Employee
        fields = ['parent', 'position', 'salary']
