from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, ProfileOverviewView, ProfileProductsView, ProfileBlogsView, ProfileUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/",LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page='/'), name="logout"),
    path("profile/", ProfileOverviewView.as_view(), name="profile"),
    path("profile/edit/", ProfileUpdateView.as_view(), name="profile_edit"),
    path("profile/products/", ProfileProductsView.as_view(), name="profile_products"),
    path("profile/blogs/", ProfileBlogsView.as_view(), name="profile_blogs"),
]
