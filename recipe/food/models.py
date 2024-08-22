from django.db import models


class Recipe(models.Model):
    Options = (
        ('VEG', 'Vegetarian'),
        ('NON-VEG', 'Non-Vegetarian'),
    )

    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    ingredients = models.TextField(null=True)
    category = models.CharField(max_length=10, choices=Options, default='VEG')

    def __str__(self):
        return self.name
