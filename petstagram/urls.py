from django.contrib import admin
from django.urls import path, include
from petstagram.views import test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('common.urls')),
    path('t/', test, name='testing'),
    path('pets/', include('pets.urls'),)
]
