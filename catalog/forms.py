import re
from django import forms
from django.core.exceptions import ValidationError

from .models import Product


FORBIDDEN_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]

pattern = r'\b(?:' + '|'.join(FORBIDDEN_WORDS) + r')\b'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "category", "image", "description"]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "form-control"})
        self.fields["price"].widget.attrs.update({"class": "form-control"})
        self.fields["description"].widget.attrs.update({"class": "form-control"})
        self.fields["category"].widget.attrs.update({"class": "form-select"})
        self.fields["image"].widget.attrs.update({"class": "form-control"})

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if re.search(pattern, name, re.IGNORECASE):
            raise ValidationError("Название содержит запрещённые слова.")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if re.search(pattern, description, re.IGNORECASE):
            raise ValidationError("Описание содержит запрещённые слова.")
        return description

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной.")
        elif price == 0:
            raise ValidationError("Цена не может быть равной нулю.")
        return price

