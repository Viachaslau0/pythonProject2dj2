from django.urls import path
from .views import RestaurantView, CategoryListView, CategoryDetailView, FoodItemListView, FoodItemDetailView

urlpatterns = [
    path('', RestaurantView.as_view(), name='home'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('fooditems/', FoodItemListView.as_view(), name='fooditem_list'),
    path('fooditems/<int:pk>/', FoodItemDetailView.as_view(), name='fooditem_detail'),
]