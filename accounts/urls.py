from django.urls import path

from .views import UserLoginView, UserLogoutView, dashboard, register_student

app_name = "accounts"

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("register/student/", register_student, name="register_student"),
    path("dashboard/", dashboard, name="dashboard"),
]
