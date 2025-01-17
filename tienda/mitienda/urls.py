from django.urls import path
from . import views

app_name = 'mitienda'

urlpatterns = [
    #Vista para mostrar los productos
    path('', views.product_list, name='product_list'),
    #Vista para mostrar los productos filtrados por categoria
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    #Vista para mostrar los detalles de un producto
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]