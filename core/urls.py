from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/whatsapp-link/', views.gerar_link_whatsapp, name='gerar_link_whatsapp'),
]
