from django.urls import path
from . import views


urlpatterns = [
    path('', views.pagina_home, name='home'),
    path('contato/', views.pagina_contato, name='contato'),
    path('projetos/', views.pagina_projetos, name='projetos')
]   
