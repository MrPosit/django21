from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        abstract = True

class Shop(BaseModel):
    SHOP_TYPES = (
        ('toy', 'Toy Shop'),
        ('phone', 'Phone Shop'),
    )
    
    name = models.CharField(max_length=100, verbose_name="Название")
    address = models.CharField(max_length=100, verbose_name="Адрес")
    type = models.CharField(max_length=50, choices=SHOP_TYPES, verbose_name="Тип магазина")
    
    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"
    
    def __str__(self):
        return f"{self.name} ({self.address})"

class Product(BaseModel):
    name = models.CharField(max_length=100, verbose_name="Название")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    description = models.TextField(verbose_name="Описание")
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="products", verbose_name="Магазин")
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
    
    def __str__(self):
        return f"{self.name} ({self.price})"

class BaseReview(models.Model):
    text = models.TextField(verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        abstract = True

class Review(BaseReview):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.text
