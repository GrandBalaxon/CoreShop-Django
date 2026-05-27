from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied
from django.forms import BooleanField


class StyleFormMixin:
    """Миксин для автоматической стилизации полей формы Bootstrap-классами."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs.setdefault('class', '')
                field.widget.attrs['class'] += ' form-check-input'
            else:
                field.widget.attrs.setdefault('class', '')
                field.widget.attrs['class'] += ' form-control'


class OwnerOrModeratorRequiredMixin(AccessMixin):
    """Проверяет, что текущий пользователь является владельцем товара."""
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.owner != request.user and not request.user.has_perm('catalog.can_unpublish_product'):
            raise PermissionDenied("Вы не можете редактировать или удалить чужой товар.")
        return super().dispatch(request, *args, **kwargs)
