from pets.models import Pet
from django.shortcuts import render

def pet_details(request, pk):
    pass

def list_pets(request):
    all_pets = Pet.objects.all()
    context = {
        'pets': all_pets,
    }
    return render(request, 'pets/pet_list.html', context)
