import category
from django.db import models
from django.urls import reverse

verbose_name_plural = 'categories'


# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)


class Meta:
    Ordering = ('Name',)
    verbose_name = 'category'
    verbose_name_plural = 'category'


def __str__(self):
    return '{}'.format(self.name)


class product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


class Meta:
    Ordering = ('Name',)
    verbose_name = 'category'
    verbose_name_plural = 'category'


def __str__(self):
    return '{}'.format(self.name)


def get_url(self):
    return reverse('shop:products_by_category', args=[self.slug])


update = models.DateTimeField(auto_now=True)

def get_url(self):
    return reverse('shop:ProdCatDetail',args=[self.category.slug,self.slug])
