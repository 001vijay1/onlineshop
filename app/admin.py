from django.contrib import admin
from .models import CustomerData,Receipt

# Register your models here.
admin.site.register(CustomerData)
admin.site.register(Receipt)