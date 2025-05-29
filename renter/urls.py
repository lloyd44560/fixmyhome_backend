from django.urls import path
from .views import RenterTestView

urlpatterns = [
    path('test/', RenterTestView.as_view()),
]
