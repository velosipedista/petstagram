from pets.models import Pet
from django.shortcuts import render

def pet_details(request, p):
    pet = Pet.objects.get(pk=p)
    context = {
        'pet': pet
    }
    return render(request, 'pets/pet_detail.html', context)

def list_pets(request):
    context = {
        'pets': Pet.objects.all(),
    }
    return render(request, 'pets/pet_list.html', context)
