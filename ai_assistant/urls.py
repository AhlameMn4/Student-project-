from django.urls import path

from .views import assistant_page

app_name = "ai_assistant"

urlpatterns = [
    path("", assistant_page, name="assistant"),
]
