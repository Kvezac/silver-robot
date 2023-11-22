from datetime import date

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator

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

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) > 15:
            raise forms.ValidationError('Имя пользователя не может содержать более 15 символов')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Это имя пользователя уже используется')
        return username

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')

        if not username:
            raise forms.ValidationError('Имя пользователя должно быть установлено')

        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['repeat_password']

        if password != confirm_password:
            raise forms.ValidationError("Пароли должны совпадать")

    def save(self):
        User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )
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
    """
        Convert local date and time for editing
    """
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        super().__init__(**kwargs)


class ProfileForm(forms.ModelForm):
    phone_regex = RegexValidator(
        regex=r'^\+7\d{10}$',
        message="Номер телефона должен быть в формате +7XXXXXXXXXX"
    )

    class Meta:
        model = Profile
        fields = ['name', 'middle_name', 'last_name', 'image', 'gender', 'date_of_bth', 'phone', 'city']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].validators.append(self.phone_regex)
        self.fields['date_of_bth'].validators.append(MinValueValidator(date.today().year - 65))
        self.fields['date_of_bth'].validators.append(MaxValueValidator(date.today().year - 18))

        for field in self.fields:
            if field == 'date_of_bth':
                self.fields[field].widget = DateInput()

            self.fields[field].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super().clean()
        for field in self.fields:
            if not cleaned_data.get(field):
                print(self.fields[field].label)
                raise forms.ValidationError(f"Поле {self.fields[field].label} не должно быть пустым")

    def profile_is_completed(self):
        pass
