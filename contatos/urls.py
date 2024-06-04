from django.urls import path
from contatos import views  

urlpatterns = [
    path('contato', views.contato),  
    path('', views.index, name='index'),
    path('contato/<int:info_id>/', views.contato, name='contato'),
    path('buscar/', views.buscar, name='buscar'),
]
