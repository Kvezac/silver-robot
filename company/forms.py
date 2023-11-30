from django import forms

from company.models import Employee


class AddEmployeeForm(forms.ModelForm):
    class Media:
        css = {
            'form-control': 'form-control',
        }

    class Meta:
        model = Employee
        fields = ['parent', 'position', 'salary', 'hire_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['hire_date'].widget.attrs['readonly'] = True
        self.fields['position'].widget.attrs['style'] = 'width:22.7ch'
