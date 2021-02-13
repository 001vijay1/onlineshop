from django.shortcuts import render,redirect
from app.form.pan_online_form import PanOnlineForm,TransactionForm
from django.contrib import messages
from app.models import CustomerData
import random




def online_pan(request):
    if request.method =='POST':
        form = PanOnlineForm(request.POST,request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            father_name = form.cleaned_data['father_name']
            dob = form.cleaned_data['dob']
            gender = form.cleaned_data['gender']
            mobile = form.cleaned_data['mobile_no']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            client_image = request.FILES['photo']
            adhaar_front = request.FILES['adhaar_front']
            adhaar_back = request.FILES['adhaar_back']
            signature = request.FILES['signature']
            insert_cus_data = CustomerData(name=name,father_name=father_name,dob=dob,gender=gender,
                mobile=mobile,email=email,address=address,client_photo=client_image,adhaar_front=adhaar_front,
                adhaar_back=adhaar_back,signature=signature)
            insert_cus_data.save()
            id = insert_cus_data.id
            return redirect('pay',id=id)
    else:
        form = PanOnlineForm()
    return render(request, 'pan_card/online_pan.html',{'form':form})

def pay(request,id):
    if request.method =='POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction_id = form.cleaned_data['transaction_id']
            registration_no = "SNPR"+str(random.randint(100000, 900000))
            cus_data = CustomerData.objects.filter(id=id).update(txn=transaction_id,registration_no=registration_no)
            return redirect('success_msg_apply_pan',new_registration=registration_no)
    else:
        form = TransactionForm()
    return render(request, 'pan_card/pay.html',{'form':form})