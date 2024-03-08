from django.db import models
from django.contrib.auth.models import User
from Category.models import CATEGORY
from django.urls import reverse
#from colorfield.fields import ColorField
from django.db import models
import uuid
#from colorfield.fields import ColorField

# Create your models here.
class SUBCATEGORY(models.Model):
    name        = models.CharField(max_length = 100,null=True)
    category    = models.ForeignKey(CATEGORY,on_delete=models.CASCADE,null=True,blank=True)
    slug        = models.CharField(max_length=100,null=True)
    messages    = models.TextField(max_length=200,null=True,blank=True)
    icon        = models.ImageField(upload_to='Subcategory',null=True,blank=True)
    is_active   = models.BooleanField(default=True)

    def __str__(self):
        return self.name + "-" + self.category.title
    class Meta:
        verbose_name_plural = 'SUBCATEGORYS'
    def get_subcategory_url(self): 
        return reverse('categoryOne',args=[self.category.slug,self.slug])
    
class ATTRIBUTES(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    description =models.TextField(max_length=250,blank=True)

    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name_plural = 'ATTRIBUTES'

class ATTRIBUTEVALUE(models.Model):
    values      = models.CharField(max_length=50,null=True,blank=True)
    valueName   = models.CharField(max_length=50,null=True,blank=True)
    attribute   =models.ForeignKey(ATTRIBUTES,on_delete=models.CASCADE,blank=True)

    def __str__(self):
        return str(self.valueName)
    class Meta:
        verbose_name_plural='ATTRIBUTEVALUE'

class BRAND(models.Model):
    supplier= models.CharField(max_length=100,null=True,blank=True)
    company = models.CharField(max_length=100,null=True,blank=True)
    maid_in = models.CharField(max_length=100,null=True,blank=True)
    image   = models.ImageField(upload_to='brandImage',blank=True,null=True)

    def __str__(self):
        return self.supplier
    class Meta:
        verbose_name_plural='BRANDS'
 
class PRODUCTS(models.Model):
    name            = models.CharField(max_length=100,null=False,blank=True)
    slug            = models.SlugField(unique=True)
    barcode         = models.CharField(max_length=50,unique=True,null=True,blank=False)
    category        = models.ForeignKey(CATEGORY,on_delete=models.CASCADE,null=True)
    subcategory     = models.ForeignKey(SUBCATEGORY,on_delete=models.CASCADE,null=True)
    description     = models.TextField(max_length=200,null=True,blank=True)
    attributevalue  = models.ManyToManyField(ATTRIBUTEVALUE,blank=True)
    brandname       = models.ForeignKey(BRAND,on_delete=models.CASCADE,null=True)
    in_stocks       = models.BooleanField(default=True)
    is_active       = models.BooleanField(default=True)
    is_discount     = models.BooleanField(default=False)
    Owner           = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    create_date     = models.DateTimeField(auto_now_add=True,blank=True)
    modified_date   = models.DateTimeField(auto_now=True,blank= True)
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name_plural = 'PRODUCTS'

    #to get single product view dynamically in procutdetails page.
    def productGet_url(self):
        return reverse('productDetails',args=[self.category.slug,self.slug])

#link for discount:https://stackoverflow.com/questions/73813646/django-models-to-calculate-discount
class PRICE(models.Model):
    product     = models.ForeignKey(PRODUCTS,on_delete=models.CASCADE) 
    saleprice   = models.DecimalField(max_digits=10, decimal_places=2,default=False,null=False)
    storeprice  = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    discount_percentage = models.DecimalField(max_digits=10, decimal_places=0,null=True,blank=True,default=0)
    mrp         = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    text        = models.TextField(max_length=50,null=True,blank=True)

    def __str__(self):
        return str(self.product)
    class Meta:
        verbose_name_plural = 'PRICES'

    @property
    def tagPrice(self):
        if self.product.is_discount==True:
             mrp = self.saleprice - (self.saleprice*self.discount_percentage)/100
             return round(mrp,2)
        else:
             mrp = self.saleprice
             return mrp

    @property
    def BDT(self):
        return "Tk %s"%self.tagPrice

unit_select =(
    ('kg','kg'),
    ('gm','gm'),
    ('litre','ltr'),
    ('pcs','pcs'),
    ('each','each'),
    ('pkg','pkg'),
)    
class STOCKS(models.Model):
    product         = models.ForeignKey(PRODUCTS,on_delete=models.CASCADE)
    quantity        = models.FloatField(null=True,blank=False)
    stocks_qty      = models.FloatField(null=True,blank=True)
    unit            = models.CharField(max_length=100,choices=unit_select,null=True)
    last_checked    = models.DateTimeField(auto_now_add=True,editable=False)
    
    
    class Meta:
        verbose_name_plural = 'STOCKS'
    def __str__(self):
        return str(self.product)

class IMAGE(models.Model):
    url             = models.ImageField(upload_to='products')
    imgLink         = models.CharField(max_length=100,null=True,blank=True)
    text            = models.TextField(max_length=50,null=True,blank=True)
    product         = models.ForeignKey(PRODUCTS,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural='IMAGES'
