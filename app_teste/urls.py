from django.urls import path
from app_teste.views import IndexView

urlpatterns = [
    path('', IndexView.as_view() ),
]
