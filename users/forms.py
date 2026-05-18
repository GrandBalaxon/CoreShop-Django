from copy import copy
from pathlib import Path

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from catalog.mixins import StyleFormMixin
from users.models import CustomUser

MAX_IMAGE_SIZE = 5 * 1024 * 1024
ALLOWED_EXTENSIONS = ('.jpg', '.jpeg', '.png')


class PhoneAvatarValidationMixin:
    """Общая валидация для телефона и аватара."""

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')

        if phone_number and isinstance(phone_number, str):
            cleaned_phone_number = copy(phone_number)

            for symbol in ["+", "-", "(", ")", " "]:
                cleaned_phone_number = cleaned_phone_number.replace(symbol, '')
            if not cleaned_phone_number.isdigit():
                raise forms.ValidationError('Номер телефона должен содержать только цифры.')

        return phone_number

    def clean_avatar(self):
        avatar = self.cleaned_data.get("avatar")
        extension = Path(avatar.name).suffix.lower()

        if extension not in ALLOWED_EXTENSIONS:
            raise forms.ValidationError(
                f"Недопустимый формат файла. Разрешенные форматы: {", ".join(ALLOWED_EXTENSIONS)}.")
        elif avatar.size > MAX_IMAGE_SIZE:
            raise forms.ValidationError("Размер файла не должен превышать 5 МБ.")

        return avatar


class CustomUserCreationForm(StyleFormMixin, PhoneAvatarValidationMixin, UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'phone_number', 'country', 'avatar']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = 'Может содержать буквы, цифры и символы @ . + - _'
        self.fields['password1'].help_text = 'Пароль должен быть не менее 8 символов, не слишком простым и не состоять только из цифр.'
        self.fields['password2'].help_text = 'Введите повторно пароль для верификации.'


class CustomUserChangeForm(StyleFormMixin, PhoneAvatarValidationMixin, UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'phone_number', 'country', 'avatar']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = 'Может содержать буквы, цифры и символы @ . + - _'
