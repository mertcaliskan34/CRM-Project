from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Record(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="records")
    
    creation_date = models.DateTimeField(auto_now_add=True)
    
    first_name = models.CharField(max_length=50)
    
    last_name = models.CharField(max_length=50)
    
    email = models.CharField(max_length=100)
    
    phone = models.CharField(max_length=20)
    
    address = models.CharField(max_length=200)
    
    city = models.CharField(max_length=50)
    
    district = models.CharField(max_length=50)
    
    country = models.CharField(max_length=50)
    
    def __str__(self):
        
        return self.first_name + "   " + self.last_name

class Product(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    
    name = models.CharField(max_length=50)
    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    description = models.TextField(max_length=200)
    
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    
    order_number = models.CharField(max_length=5)
    
    customer = models.ForeignKey(Record, on_delete=models.CASCADE, related_name="orders")
    
    products = models.ManyToManyField(Product, related_name="orders")
    
    amount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)])
    
    ORDER_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('shipping', 'Shipping'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    
    status = models.CharField(
        max_length=10, 
        choices=ORDER_STATUS_CHOICES,
        default='pending'
    )
    
    creation_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Order {self.order_number} - {self.get_status_display()}"

class Review(models.Model):
    
    customer = models.ForeignKey(Record, on_delete=models.CASCADE, related_name="reviews")
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    
    review_text = models.TextField(max_length=200)
    
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ""