from django.db import models
from django.db.models.deletion import CASCADE

class category_master(models.Model):
    category_name = models.CharField(max_length=200,null=True,unique=True)
    class Meta:
        db_table = 'Category_master'

class subcategory_master(models.Model):
    category = models.ForeignKey(category_master, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=200,null=True,unique=True)
    class Meta:
        db_table = 'subcategory_master'

class product_master(models.Model):
    name = models.CharField(max_length=200,null=True)
    company_name = models.CharField(max_length=200,null=True,blank=True)
    image=models.ImageField(null=True,blank=True)
    model_year = models.IntegerField(null=True,blank=True,default=2000) 
    running_km = models.IntegerField(blank=True,default=0)
    fuel_type = models.CharField(max_length=30,null=True,blank=True)
    p_reg_date = models.DateField()
    subcategory = models.ForeignKey(subcategory_master,on_delete=models.CASCADE)
    class Meta:
        db_table = 'product_master' 
class Auction_info(models.Model):
    product =models.OneToOneField(product_master,on_delete=CASCADE)
    start_dateTimeInfo = models.DateTimeField()
    payment_dateTimeInfo = models.DateTimeField()
    basePrice = models.IntegerField(null=True,blank=True)
    class Meta:
        db_table ='Auction_info'






