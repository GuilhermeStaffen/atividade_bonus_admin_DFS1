
from django.urls import path

from restaurante import views

urlpatterns = [
    path('', views.produtos, name='home'),
    path('cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
]