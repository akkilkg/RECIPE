from .models import Recipe
from rest_framework import generics
from rest_framework.response import Response
from .serializers import FoodRecipeSerializer

class FoodRecipeListCreateView(generics.ListCreateAPIView):
    serializer_class = FoodRecipeSerializer

    def get_queryset(self):
        queryset = Recipe.objects.all()
        category = self.request.query_params.get('category')
        if category in dict(Recipe.Options):
            queryset = queryset.filter(category=category)
        return queryset

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

class FoodRecipeUpdateView(generics.UpdateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = FoodRecipeSerializer

    def patch(self, request):
        serializer = self.get_serializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
