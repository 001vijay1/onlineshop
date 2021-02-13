from django.urls import path
from app.View.account.login import login,logout
from app.View.pan_card.online_pan_card import online_pan,pay
from app.View.receipt.receipt import download_receipt,receipt,upload_receipt,check_uploaded_receipt
from app.View.customer_list.customer_data import customer_list,customer_details,cust_certificate_list,\
    cust_certificate_details,main_list
from app.View.delete.delete_data import delete_customer,delete_receipt,delete_cust_certificate,delete_certificate
from app.View.govt_scheme.govt_scheme import govt_scheme
from app.View.gst.online_gst import online_gst
from app.View.success_message.success_msg import success_msg_apply_pan,success_msg_apply_certificate
from app.View.certificate.certificate import certificate,certificate_pay
from app.View.certificate.uploaded_certificate import upload_certificate,download_certificate,uploaded_certificate_list,\
    get_certificate_by_id

from app.views import developer



urlpatterns = [
    path('pan_online',online_pan, name='online_pan'),
    path('pay/<int:id>',pay, name='pay'),
    path('main_list',main_list, name='main_list'),
    path('customer_list',customer_list, name='customer_list'),
    path('login',login, name='login'),
    path('logout',logout, name='logout'),
    path('download_receipt',download_receipt, name='download_receipt'),
    path('receipt/<int:id>',receipt, name='receipt'),
    path('upload_receipt',upload_receipt, name='upload_receipt'),
    path('customer_details/<int:id>',customer_details, name='customer_details'),
    path('check_uploaded_receipt',check_uploaded_receipt, name='check_uploaded_receipt'),
    path('delete_customer/<int:id>',delete_customer, name='delete_customer'),
    path('success_msg_apply_pan/<str:new_registration>',success_msg_apply_pan, name='success_msg_apply_pan'),
    path('delete_receipt/<int:id>',delete_receipt, name='delete_receipt'),
    path('online_gst',online_gst, name='online_gst'),
    path('govt_scheme',govt_scheme, name='govt_scheme'),
    path('certificate',certificate, name='certificate'),
    path('certificate_pay/<int:id>/<int:rs>',certificate_pay, name='certificate_pay'),
    path('success_msg_apply_certificate/<str:new_registration>',success_msg_apply_certificate, name='success_msg_apply_certificate'),
    path('cust_certificate_list',cust_certificate_list, name='cust_certificate_list'),
    path('cust_certificate_details/<int:id>',cust_certificate_details, name='cust_certificate_details'),
    path('delete_cust_certificate/<int:id>',delete_cust_certificate, name='delete_cust_certificate'),
    path('upload_certificate',upload_certificate, name='upload_certificate'),
    path('download_certificate',download_certificate, name='download_certificate'),
    path('uploaded_certificate_list',uploaded_certificate_list, name='uploaded_certificate_list'),
    path('get_certificate_by_id/<int:id>',get_certificate_by_id, name='get_certificate_by_id'),
    path('delete_certificate/<int:id>',delete_certificate, name='delete_certificate'),
    path('developer',developer, name='developer'),
    
]
