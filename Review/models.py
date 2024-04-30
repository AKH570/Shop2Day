from django.db import models
#from django.contrib.auth.models import User
from Accounts.models import User
from Inventory.models import PRODUCTS
# Create your models here.

class Reviews(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,blank=False,null=True,db_column='author')
    product = models.ForeignKey(PRODUCTS,on_delete=models.CASCADE,blank=False,null=True,db_column='product')
    message = models.TextField(max_length=200,blank=True,null=True)
    # comments = models.TextField(max_length=200,blank=True,null=True)
    rating = models.FloatField(null=True,blank=True)
    ip = models.CharField(max_length=100,blank=True)
    status = models.BooleanField(default=True)
    commentDate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.message)
    # def __str__(self):
    #     return str(self.product)
    class Meta:
        verbose_name_plural = 'REVIEWS'
    # class Meta:
    #     managed = False
    #     db_table = 'b2c_features\".\"Reviews'