from django.shortcuts import redirect,render
from app.models import UploadedCertificate
from app.form.certificate import DownloadCertificateForm,UploadCertificateForm
from django.contrib import messages


def upload_certificate(request):
    if request.method=='POST':
        form = UploadCertificateForm(request.POST,request.FILES)
        if form.is_valid():
            registration_no = form.cleaned_data['registration_no']
            certificate = request.FILES['certificate']
            insert_certificate = UploadedCertificate(registration_no=registration_no,certificate=certificate)
            insert_certificate.save()
            return redirect('uploaded_certificate_list')
    else:
        form = UploadCertificateForm()
    return render(request, 'certificate/upload_certificate/upload_certificate.html',{'form':form})

def uploaded_certificate_list(request):
    data = UploadedCertificate.objects.all()
    return render(request, 'certificate/upload_certificate/uploaded_certificate_list.html',{'data':data})

def download_certificate(request):
    if request.method=='POST':
        form = DownloadCertificateForm(request.POST)
        if form.is_valid():
            registration_no = form.cleaned_data['registration_no']
            data = UploadedCertificate.objects.filter(registration_no=registration_no)
            if data:
                id = data[0].id
                return redirect('get_certificate_by_id',id=id)
            else:
                messages.error(request, 'Certificate does not exist, Please wait or call:-9999677991.')
    else:
        form = DownloadCertificateForm()
    return render(request, 'certificate/upload_certificate/download_certificate.html',{'form':form})

def get_certificate_by_id(request,id):
    cust_data = UploadedCertificate.objects.filter(id=id)
    cust_certificate = cust_data[0].certificate
    return render(request,'receipt/receipt.html',{'cust_receipt':cust_certificate})
