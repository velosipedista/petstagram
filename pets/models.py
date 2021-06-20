from django.core.exceptions import ValidationError
from django.db import models

# def is_positive(value):
#     if value <= 0:
#         raise ValidationError

class Pet(models.Model):
    TYPE_CHOICE_DOG = 'dog'
    TYPE_CHOICE_CAT = 'cat'
    TYPE_CHOICE_PARROT = 'parrot'

    TYPE_CHOICES = [
        (TYPE_CHOICE_DOG, 'Dog'),
        (TYPE_CHOICE_CAT, 'Cat'),
        (TYPE_CHOICE_PARROT, 'Parrot'),
    ]
    type  = models.CharField(
        max_length=6,
        choices=TYPE_CHOICES,
    )
    name = models.CharField(
        max_length=6,
        null=True,
        blank=True,
    )
    age = models.PositiveIntegerField()

    description = models.TextField (
        null=True,
        blank=True,
    )
    image_url = models.URLField(
        null=True,
        blank=True,
    )


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
