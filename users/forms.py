from pathlib import Path

from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import CustomUser

MAX_IMAGE_SIZE = 5 * 1024 * 1024
ALLOWED_EXTENSIONS = ('.jpg', '.jpeg', '.png')


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = '__all__'

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Номер телефона должен содержать только цифры.')
        return phone_number

    def clean_avatar(self):
        avatar = self.cleaned_data.get("avatar")
        extension = Path(avatar.name).suffix.lower()

        if extension not in ALLOWED_EXTENSIONS:
            raise forms.ValidationError(f"Недопустимый формат файла. Разрешенные форматы: {", ".join(ALLOWED_EXTENSIONS)}.")
        elif avatar.size > MAX_IMAGE_SIZE:
            raise forms.ValidationError("Размер файла не должен превышать 5 МБ.")

        return avatar
