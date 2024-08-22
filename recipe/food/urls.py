from django.urls import path
from .views import FoodRecipeListCreateView, FoodRecipeUpdateView

urlpatterns = [
    path('recipes/', FoodRecipeListCreateView.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', FoodRecipeUpdateView.as_view(), name='recipe-update'),
]
