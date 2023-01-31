from django.db import models

# Create your models here.
class Solar(models.Model):
    ct = models.CharField(max_length=255)
    week= models.CharField(max_length=11,blank=True,default=1)
    affiliate= models.CharField(max_length=255)
    pid= models.CharField(max_length=255)
    install_partner= models.CharField(max_length=255)
    customer_name= models.CharField(max_length=255)
    sales_rep_name=models.CharField(max_length=255)
    kw = models.FloatField(default=0.00)
    inactive_date= models.DateTimeField(auto_now_add=True)
    cancel=models.FloatField(default=1,blank=True,null=True)
    approved_date=models.DateTimeField(auto_now_add=True)
    m1_date= models.DateTimeField(auto_now_add=True)
    m2_date=models.DateTimeField(auto_now_add=True)
    state= models.CharField(max_length=255)
    product= models.CharField(max_length=255)
    gross_account_value=models.FloatField(default=00.00)
    epc= models.FloatField()
    net_epc= models.FloatField()
    dealer_fee_percentage =models.FloatField()
    dealer_fee_dollar   = models.FloatField()
    shows= models.FloatField()
    redline= models.FloatField()
    total_for_acct = models.FloatField()
    prev_paid= models.FloatField()
    last_date_pd= models.DateTimeField(auto_now_add=True)
    m1_this_week = models.FloatField()
    install_m2_this_week= models.FloatField() 
    prev_deducted = models.FloatField()
    cancel_fee = models.FloatField()
    cancel_deduction= models.CharField(max_length=11)
    lead_cost = models.FloatField(default=1,blank=True,null=True)
    ad_pay_back = models.FloatField()
    total_in_period= models.FloatField()