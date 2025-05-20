from django.urls import path
from .views import vistaPrueba

#si no se llama la variable asi, tendremos un error
urlpatterns = [
    path('prueba/', vistaPrueba),
]