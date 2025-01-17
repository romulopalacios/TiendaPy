from django.shortcuts import get_object_or_404, render
from .models import Category, Product

# Create your views here.

#Vista para mostrar los productos
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    #Filtrar por categoría

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'mitienda/product/list.html', {'category': category, 'categories': categories, 'products': products})

#Vista para mostrar los detalles de un producto
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'mitienda/product/detail.html', {'product': product})