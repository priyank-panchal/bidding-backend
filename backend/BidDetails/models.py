from django.db import models
from django.contrib.auth.models import User
from products.models import product_master
class bids_master(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    product =models.ForeignKey(product_master, on_delete=models.CASCADE)
    bidAmount = models.PositiveBigIntegerField(null=True)
    dateTime_bid = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'bids_master'

class order_item_master(models.Model):
    product =models.OneToOneField(product_master, on_delete=models.CASCADE,null=True,blank=True)
    bid = models.OneToOneField(bids_master,on_delete=models.CASCADE,null=True,blank=True)
    payment_status = models.BooleanField(blank=True,null=True)
    amount = models.PositiveBigIntegerField(null=True) 
    class Meta:
        db_table = 'order_item_master' 

