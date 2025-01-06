from django.urls import path
from . import views

urlpatterns = [
    path('', views.fashion_item_list, name='fashion_item_list'),
    path('<int:pk>/', views.fashion_item_detail, name='fashion_item_detail'),
    path('create/', views.fashion_item_create, name='fashion_item_create'),
    path('<int:pk>/update/', views.fashion_item_update, name='fashion_item_update'),
    path('<int:pk>/delete/', views.fashion_item_delete, name='fashion_item_delete'),
]
