from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView

from users.forms import CustomUserCreationForm
from users.models import CustomUser


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = '/'


class CustomUserDetailsView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'users/profile.html'
    context_object_name = 'profile_user'

    def get_object(self, queryset=None):
        return self.request.user
