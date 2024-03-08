from django.db import models
from django.contrib.auth.models import User
from Inventory.models import PRODUCTS
# Create your models here.

class Reviews(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    email  = models.EmailField(max_length=100,blank=False,null=True)
    message = models.CharField(max_length=300,blank=True)
    picture = models.ImageField(upload_to='Reviews',null=True,blank=True)
    product = models.ForeignKey(PRODUCTS,on_delete=models.CASCADE,blank=True)
    noOfReview = models.PositiveIntegerField()
    commentDate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.author}'
    class Meta:
        verbose_name_plural = 'REVIEWS'