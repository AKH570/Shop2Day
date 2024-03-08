from django.db import models
from django.contrib.auth.models import User
# from Category.models import CATEGORY
# from Inventory.models import ATTRIBUTEVALUE,BRAND

# Create your models here.

# class INDEXPRODUCT(models.Model):
#     name            = models.CharField(max_length=100,null=True,blank=True)
#     slug            = models.SlugField()
#     category        = models.ForeignKey(CATEGORY,on_delete=models.CASCADE,null=True)
#     description     = models.TextField(max_length=200,null=True,blank=True)
#     attributevalue  = models.ManyToManyField(ATTRIBUTEVALUE)
#     brandname       = models.ForeignKey(BRAND,on_delete=models.CASCADE,null=True)
#     stocks          = models.IntegerField(null=True,default=0)
#     images          = models.ImageField(upload_to='indexproduct')
#     is_active       = models.BooleanField(default=True)
#     Owner           = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
#     create_date     = models.DateTimeField(auto_now_add=True,blank=True)
#     modified_date   = models.DateTimeField(auto_now=True,blank= True)

#     class Meta:
#         verbose_name_plural = 'INDEX PRODUCTS'
#     def __str__(self): 
#         return str(self.name)

# class PRICE(models.Model):
#     product     = models.ForeignKey(INDEXPRODUCT,on_delete=models.CASCADE) 
#     saleprice   = models.DecimalField(max_digits=4, decimal_places=2,default=False,null=False)
#     storeprice  = models.DecimalField(max_digits=4, decimal_places=2,null=True)
#     discount    = models.DecimalField(max_digits=4, decimal_places=2,null=True)
#     text        = models.TextField(max_length=100,null=True)

#     def __str__(self):
#         return str(self.name)
#     class Meta:
#         verbose_name_plural = 'PRICES'

#     @property
#     def BDT(self):
#         return "Tk %s"%self.saleprice