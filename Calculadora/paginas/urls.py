from django.urls import path
from .views import FormularioView, IndexView

urlpatterns = [
    #path('endereço/', MihnaView.as_view(), name='nome-da-url')
    path('', IndexView.as_view(), name='inicio'),
    path('form/', FormularioView.as_view(), name = 'formulario'),
]