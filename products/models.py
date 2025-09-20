from django.db import models

# Create your models here.
# - Category
# - Product (category bilan bog'langan, narx, miqdor, rasm)

class Category(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(120)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.SmallIntegerField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.name}  | {self.price}"
    
    