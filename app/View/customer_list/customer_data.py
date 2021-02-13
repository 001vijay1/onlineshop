from django.shortcuts import redirect,render
from app.models import CustomerData,Certificate


def main_list(request):
    return render(request,'customer_list/main_list.html')

def customer_list(request):
    data = CustomerData.objects.all()
    return render(request,'customer_list/customer_list.html',{'data':data})

def cust_certificate_list(request):
    data = Certificate.objects.all()
    return render(request, 'customer_list/cust_certificate_list.html',{'data':data})



def customer_details(request,id):
    cust_data = CustomerData.objects.filter(id=id)
    data = cust_data[0]
    return render(request,'customer_list/customer_details.html',{'data':data})

def cust_certificate_details(request,id):
    cust_data = Certificate.objects.filter(id=id)
    data = cust_data[0]
    return render(request, 'customer_list/cust_certificate_details.html',{'data':data})