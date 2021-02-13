from django.shortcuts import render,redirect

# Create your views here.

def success_msg_apply_pan(request,new_registration):
    return render(request, 'success_message/success_msg_apply_pan.html',{'new_registration':new_registration})

def success_msg_apply_certificate(request,new_registration):
    return render(request, 'success_message/success_msg_apply_certificate.html',{'new_registration':new_registration})