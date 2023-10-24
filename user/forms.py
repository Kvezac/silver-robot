from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

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
            'class': "form-control",
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


class ProfileForm(forms.ModelForm):
    name = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "InputName",
            'placeholder': "Имя",
        }),
    )
    middle_name = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "InputMiddleName",
            'placeholder': "Отчество",
        }),
    )
    last_name = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "InputLastName",
            'placeholder': "Фамилия",
        }),
    )
    image = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'class': "form-control-file",
            'id': "InputImage",
        }),
    )
    gender = forms.ChoiceField(
        choices=Profile.GENDER_CHOICES,
        required=False,
        widget=forms.Select(attrs={
            'class': "form-control",
            'id': "InputGender",
        }),
    )
    date_of_bth = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': "form-control",
            'id': "InputDateOfBirth",
        }),
    )
    phone = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "InputPhone",
            'placeholder': "Телефон",
        }),
    )
    city = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "InputCity",
            'placeholder': "Город",
        }),
    )

    class Meta:
        widgets = {
            'last_name': forms.TextInput(attrs={
                'class': "form-control",
                'id': "InputLastName",
                'placeholder': "Фамилия",
            }),
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'id': "InputName",
                'placeholder': "Имя",
            }),
            'middle_name': forms.TextInput(attrs={
                'class': "form-control",
                'id': "InputMiddleName",
                'placeholder': "Отчество",
            }),
            'image': forms.FileInput(attrs={
                'class': "form-control-file",
                'id': "InputImage",
            }),
            'gender': forms.Select(attrs={
                'class': "form-control",
                'id': "InputGender",
            }),
            'date_of_bth': forms.DateInput(attrs={
                'class': "form-control",
                'id': "InputDateOfBirth",
            }),
            'phone': forms.TextInput(attrs={
                'class': "form-control",
                'id': "InputPhone",
                'placeholder': "Телефон",
            }),
            'city': forms.TextInput(attrs={
                'class': "form-control",
                'id': "InputCity",
                'placeholder': "Город",
            }),
        }
        model = Profile
        fields = ['name', 'middle_name', 'last_name', 'image', 'gender', 'date_of_bth', 'phone', 'city']
