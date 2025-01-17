from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    class Meta:
        ordering = ('name',)
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name = 'category'
    def __str__(self):
        return self.name
    
    #Para obtener la URL absoluta de la categoría
    def get_absolute_url(self):
        return reverse('mitienda:product_list_by_category', args=[self.slug])
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'product'
        ordering = ('name',)

    def __str__(self):
        return self.name
    
    #Para obtener la URL absoluta del producto
    def get_absolute_url(self):
        return reverse('mitienda:product_detail', args=[self.id, self.slug])
    