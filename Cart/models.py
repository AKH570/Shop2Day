from django.db import models
#from django.contrib.auth.models import User
from Accounts.models import User
from Inventory.models import PRODUCTS,STOCKS,PRICE,IMAGE

# Create your models here.

class CART(models.Model):
    user        = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    product     = models.ForeignKey(PRODUCTS,on_delete=models.CASCADE)
    qty         = models.PositiveIntegerField()
    price       = models.ForeignKey(PRICE,on_delete=models.CASCADE,null=True,blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.product)
    # def __str__(self):
    #     return f'{self.qty}x{self.product}'
    class Meta:
        verbose_name_plural='CARTS'
   
#    this func is for subtotal amt in cart page that is not completed
    # def qnty_price(self):
    #     return (self.product.category.slug)
        # print(self.qty * self.product.price.mrp)