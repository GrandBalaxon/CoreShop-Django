from secrets import token_hex

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView

from blog.models import BlogPost
from catalog.models import Product
from config.settings import EMAIL_HOST_USER
from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import CustomUser


class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{token}/"
        send_mail(
            subject="Подтверждение почты",
            message=f"Для подтверждения почты перейдите по следующей ссылке - {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'users/profile_edit.html'
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("users:profile")

    def get_object(self, queryset=None):
        return self.request.user


class ProfileOverviewView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'users/profile_overview.html'
    context_object_name = 'profile_user'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # Количество товаров
        context['products_count'] = Product.objects.filter(owner=user).count()

        # Сумма просмотров всех статей пользователя
        total_views = BlogPost.objects.filter(author=user).aggregate(total=Sum('views_count'))['total'] or 0
        context['total_blog_views'] = total_views

        # Последний товар
        context['last_product'] = Product.objects.filter(owner=user).order_by('-created_at').first()

        # Последняя статья
        context['last_blogpost'] = BlogPost.objects.filter(author=user).order_by('-created_at').first()

        return context


class ProfileProductsView(ProfileOverviewView):
    template_name = 'users/my_products.html'


class ProfileBlogsView(ProfileOverviewView):
    template_name = 'users/my_blogs.html'


def email_verification(request, token):
    user = get_object_or_404(CustomUser, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:profile"))
