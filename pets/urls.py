from pets.views import list_pets, pet_details
from django.urls import path


urlpatterns = [
    path('', list_pets, name='list_pets'),
    path('details/<int:p>', pet_details, name='pet_detail')    
]