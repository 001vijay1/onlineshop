from django.shortcuts import render,redirect

# Create your views here.
def developer(request):
    return render(request,'developer/developer.html')


