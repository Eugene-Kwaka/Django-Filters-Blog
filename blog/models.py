from django.db import models

# Create your models here.
class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    )
    product = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True, 
    choices=CATEGORY)
    status = models.CharField(max_length=100, null=True, 
    choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, 
    null=True)

    def __str__(self):
        return self.product


