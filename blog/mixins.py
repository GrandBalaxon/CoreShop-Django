from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied


class AuthorRequiredMixin(AccessMixin):
    """Проверяет, что текущий пользователь является автором статьи."""
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author != request.user:
            raise PermissionDenied("Вы не можете редактировать или удалить чужую статью.")
        return super().dispatch(request, *args, **kwargs)
