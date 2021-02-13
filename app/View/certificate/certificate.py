from django.shortcuts import redirect,render
from app.form.certificate import CertificateForm
from app.form.pan_online_form import TransactionForm
from django.contrib import messages
from app.models import Certificate
import random



def certificate(request):
    if request.method =='POST':
        form = CertificateForm(request.POST,request.FILES)
        if form.is_valid():
            income = request.POST.get('income',False)
            if income!=False:
                income='Income'
            else:
                income = ''
            domicile = request.POST.get('domicile',False)
            if domicile!=False:
                domicile ='Domicile'
            else:
                domicile = ''
            caste = request.POST.get('caste',False)
            if caste!=False:
                caste = 'Caste'
            else:
                caste = ''
            if((income=='' and domicile=='') and caste==''):
                messages.error(request,'कृपया आय , जाति , निवास प्रमाण पत्र में से कोई चूने.')
            else:
                rupee = request.POST['rupee']
                service = income+" + "+domicile+" + "+caste
                name = form.cleaned_data['name']
                father_name = form.cleaned_data['father_name']
                mother_name = form.cleaned_data['mother_name']
                mobile = form.cleaned_data['mobile_no']
                mother_name = form.cleaned_data['mother_name']
                client_photo = request.FILES['client_photo']
                adhaar_front = request.FILES['adhaar_front']
                adhaar_back = request.FILES['adhaar_back']
                insert_data = Certificate(name=name,father_name=father_name,mother_name=mother_name,mobile=mobile,
                client_photo=client_photo,adhaar_front=adhaar_front,adhaar_back=adhaar_back,service=service)
                insert_data.save()
                id = insert_data.id
                return redirect('certificate_pay',id=id,rs=rupee)
            
    else:
        form = CertificateForm()
    return render(request, 'certificate/certificate.html',{'form':form})

def certificate_pay(request,id,rs):
    if request.method =='POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            registration_no = "SNCR"+str(random.randint(100000, 900000))
            transaction_id = form.cleaned_data['transaction_id']
            cus_data = Certificate.objects.filter(id=id).update(txn=transaction_id,registration_no=registration_no)
            return redirect('success_msg_apply_certificate',new_registration=registration_no)
    else:
        form = TransactionForm()
    return render(request,'certificate/certificate_pay.html',{'form':form,'rs':rs})