from django.db import models
from Accounts.models import User

# Create your models here.

class Order(models.Model):
    STATUS =(
        ('New','New'),
        ('Accepted','Accepted'),
        ('Cancelled','Cancelled'),
    )
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    orderNo = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=20,blank=True)
    email = models.EmailField(max_length=30)
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=50,default='Bangladesh')
    district = models.CharField(max_length=30,blank=True)
    billAmount = models.FloatField()
    paymentMethod = models.CharField(max_length=50,blank=True)
    status = models.CharField(max_length=20,choices=STATUS,default='New')
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    checked_by = models.CharField(max_length=20,blank=True)

    @property
    def name(self):
        return f'{self.first_name}{self.last_name}'
    def __str__(self):
        return self.orderNo

