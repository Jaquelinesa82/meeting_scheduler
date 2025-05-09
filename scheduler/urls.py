from django.urls import path
from . import views 

urlpatterns = [
    path('teste/', views.teste_view, name='teste'),
]