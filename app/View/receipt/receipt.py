from django.shortcuts import render,redirect
from app.form.receipt import DownloadReceiptForm,UploadReceiptForm
from django.contrib import messages
from app.models import Receipt



def download_receipt(request):
    if request.method=='POST':
        form = DownloadReceiptForm(request.POST)
        if form.is_valid():
            registration_no = form.cleaned_data['registration_no']
            access_data = Receipt.objects.filter(registration_no=registration_no)
            if access_data:
                id = access_data[0].id
                return redirect('receipt',id=id)
            else:
                messages.error(request, 'Receipt does not exist, Please try after sometime.')
    else:
        form = DownloadReceiptForm()
    return render(request, 'receipt/download_receipt.html',{'form':form})

def receipt(request,id):
    cust_data = Receipt.objects.filter(id=id)
    cust_receipt = cust_data[0].receipt
    return render(request,'receipt/receipt.html',{'cust_receipt':cust_receipt})

def upload_receipt(request):
    if request.method=='POST':
        form = UploadReceiptForm(request.POST,request.FILES)
        if form.is_valid():
            registration_no = form.cleaned_data['registration_no']
            receipt = request.FILES['receipt']
            insert_receipt = Receipt(registration_no=registration_no,receipt=receipt)
            insert_receipt.save()
            messages.success(request, 'Receipt uploaded successfully!')
            return redirect('check_uploaded_receipt')
    else:
        form = UploadReceiptForm()
    return render(request,'receipt/upload_receipt.html',{'form':form})

def check_uploaded_receipt(request):
    receipt = Receipt.objects.all()
    return render(request, 'receipt/check_uploaded_receipt.html',{'receipt':receipt})