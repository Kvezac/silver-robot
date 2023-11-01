from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from config import settings
from user.models import Profile


class SigUpForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "InputUsername",
            'placeholder': "Имя пользователя",
        }),
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control mt-2",
            'id': "InputPassword",
            'placeholder': "Введите Пароль",
        }),
    )
    repeat_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control mt-2",
            'id': "ReInputPassword",
            'placeholder': "Повторите пароль",
        }),
    )

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['repeat_password']

        if password != confirm_password:
            raise forms.ValidationError(
                "Пароли не совпадают"
            )

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )
        user.save()
        auth = authenticate(**self.cleaned_data)
        return auth


class SignInForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control mt-2",
            'id': "InputUsername",
            'placeholder': "Введите логин"
        })
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control mt-2",
            'id': "InputPassword",
            'placeholder': "Введите пароль",
        })
    )


class DateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        super().__init__(**kwargs)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'middle_name', 'last_name', 'image', 'gender', 'date_of_bth', 'phone', 'city']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            if field == 'date_of_bth':
                self.fields[field].widget = DateInput()

            self.fields[field].widget.attrs.update({'class': 'form-control'})
