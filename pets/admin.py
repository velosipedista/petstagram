from django.contrib import admin
from pets.models import Pet

class PetAdmin(admin.ModelAdmin):
    list_display = ['name','type','age']

admin.site.register(Pet, PetAdmin)
# admin.site.register(PetAdmin)
