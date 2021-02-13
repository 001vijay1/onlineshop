from django.shortcuts import redirect,render
from app.models import CustomerData,Receipt,Certificate,UploadedCertificate
from django.contrib import messages




def delete_customer(request,id):
    cust_data = CustomerData.objects.filter(id=id).delete()
    messages.success(request, 'Customer deleted successfully!')
    return redirect('customer_list')

def delete_receipt(request,id):
    receipt = Receipt.objects.filter(id=id).delete()
    messages.success(request, 'Receipt deleted successfully!')
    return redirect('check_uploaded_receipt')

def delete_cust_certificate(request,id):
    receipt = Certificate.objects.filter(id=id).delete()
    messages.success(request, 'Customer deleted successfully!')
    return redirect('cust_certificate_list')

def delete_certificate(request,id):
    receipt = UploadedCertificate.objects.filter(id=id).delete()
    messages.success(request, 'Certificate deleted successfully!')
    return redirect('uploaded_certificate_list')