from django import forms

from company.models import Employee
from user.forms import DateInput


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'position', 'hire_date', 'salary']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            if field == 'hire_date':
                self.fields[field].widget = DateInput()

            self.fields[field].widget.attrs.update({'class': 'form-control'})
