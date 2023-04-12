from django.db import models
from accounts.models import Profile
from django.core.validators import MaxValueValidator


class Category(models.Model):
    ELECTRONICS = 'electronics'
    BOOKS = 'books'
    CLOTHING = 'clothing'
    HOME = 'home'
    COLLECTIBLES = 'collectibles'
    SPORTING_GOODS = 'sporting_goods'

    CATEGORY_CHOICES = [
        ('electronics', 'Electronics'),
        ('books', 'Books'),
        ('clothing', 'Clothing'),
        ('home', 'Home'),
        ('collectibles', 'Collectibles'),
        ('sporting_goods', 'Sporting Goods'), 
    ]

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default=ELECTRONICS,
    )

    def __str__(self):
        return self.category
class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    seller = models.ForeignKey(Profile, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(Profile, on_delete=models.PROTECT)
    content = models.TextField(max_length=1000)
    rating = models.IntegerField(validators=[MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'{self.product} - {self.rating}')
