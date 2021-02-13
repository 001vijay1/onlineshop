from django.shortcuts import render,redirect

def online_gst(request):
    return render(request,'gst/online_gst.html')