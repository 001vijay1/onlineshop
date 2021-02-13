from django.shortcuts import redirect,render

def govt_scheme(request):
    return render(request,'govt_scheme/govt_scheme.html')