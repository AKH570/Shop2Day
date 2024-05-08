from django.db import models
#from django.contrib.auth.models import User
from Accounts.models import User
from Inventory.models import PRODUCTS,STOCKS,PRICE,IMAGE

# Create your models here.

class CART(models.Model):
    user        = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    product     = models.ForeignKey(PRODUCTS,on_delete=models.CASCADE)
    qty         = models.PositiveIntegerField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.user
    class Meta:
        verbose_name_plural='CARTS'
