from pets.views import list_pets
from django.urls import path


urlpatterns = [
    path('', list_pets, name='list_pets'),
]