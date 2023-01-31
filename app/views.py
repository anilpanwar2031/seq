from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse
import pandas as pd
from app.models import Solar
from app import cron
data= pd.read_excel(r"C:\Users\chand\Downloads\VANTAGE SOLAR POWER_01.27.23.xlsx")
data= data.iloc[:,1:56]
print(data.head())
data.columns
print(data.size)
print(data.shape)
data = data.set_axis(['ct','affiliate','pid','install_partner','customer_name','sales_rep_name','kw','inactive_date','cancel','approved_date','m1_date','m2_date','state','product','gross_account_value','epc','net_epc','dealer_fee_percentage','dealer_fee_dollar','shows','redline','total_for_acct','prev_paid','last_date_pd','m1_this_week','install_m2_this_week','prev_deducted','cancel_fee','cancel_deduction','lead_cost','ad_pay_back','total_in_period'], axis='columns', inplace=False)
data = pd.DataFrame(data)
data=data.fillna(0)
data['cancel_fee']= data['cancel_fee'].astype(float)
data['ct']= data['ct'].astype(object)
data['lead_cost']= data['lead_cost'].astype(float)
data['cancel_deduction']= data['cancel_deduction'].astype(object)
data['total_in_period']= data['total_in_period'].astype(float)
data['ad_pay_back']= data['ad_pay_back'].astype(float)
# print(data.dtypes)
# dicts = data.to_dict()
data.fillna("-",inplace=True)

print(data)
d =cron.getDataAndDate()
print("week",d)
for i in range(len(data)):
    s = Solar(ct=data.iloc[i,0],affiliate= data.iloc[i,1],pid=data.iloc[i,2],install_partner= data.iloc[i,3],customer_name=data.iloc[i,4],sales_rep_name=data.iloc[i,5],kw=data.iloc[i,6],inactive_date=data.iloc[i,7],cancel=data.iloc[i,8],approved_date=data.iloc[i,9],m1_date=data.iloc[i,10],m2_date=data.iloc[i,11],state=data.iloc[i,12],product=data.iloc[i,13],gross_account_value=data.iloc[i,14],epc=data.iloc[i,15],net_epc=data.iloc[i,16],dealer_fee_percentage=data.iloc[i,17],dealer_fee_dollar=data.iloc[i,18],shows=data.iloc[i,19],redline=data.iloc[i,20],total_for_acct=data.iloc[i,21],prev_paid=data.iloc[i,22],last_date_pd=data.iloc[i,23],m1_this_week=data.iloc[i,24],install_m2_this_week=data.iloc[i,25],prev_deducted=data.iloc[i,26],cancel_fee=data.iloc[i,27],cancel_deduction=data.iloc[i,28],ad_pay_back=data.iloc[i,29],total_in_period=data.iloc[i,30],week=d)
    s.save()


# s = Solar(week=d)
# s.save()
