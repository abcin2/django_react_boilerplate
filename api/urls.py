from django.urls import path
from .views import ModelOneView

urlpatterns = [
    path('', ModelOneView.as_view())
]
