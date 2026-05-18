from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from blog.models import BlogPost
from catalog.models import Product
from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import CustomUser


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = '/'


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
