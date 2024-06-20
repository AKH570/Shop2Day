from django.db import models
from django.urls import reverse

# STEP 3 Create your models here.

# Table # 1
class CATEGORY(models.Model):
    title       = models.CharField(max_length=50)
    slug        = models.CharField(max_length=50)
    description = models.TextField(max_length=250,null=True,blank=True)
    cat_image   = models.ImageField(upload_to='categories',blank=True)
    is_active   =  models.BooleanField(default=True)

    class Meta():
        verbose_name_plural = "CATEGORYIES"

    # to get category dynamically from html template
    def get_category_url(self): 
        return reverse('cat_item',args=[self.slug])

    def __str__(self):
        return self.title