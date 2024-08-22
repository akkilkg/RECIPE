from rest_framework import serializers
from .models import Recipe

class FoodRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

    def validate_name(self, value):
        if Recipe.objects.filter(name=value).exists():
            raise serializers.ValidationError("This recipe already exists..")
        return value
