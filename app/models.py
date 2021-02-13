from django.db import models
import os
from django.dispatch import receiver

# Create your models here.

def _delete_file(path):
    """ Deletes file from filesystem. """
    if os.path.isfile(path):
        os.remove(path)

class CustomerData(models.Model):
    name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    dob = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    client_photo = models.ImageField(upload_to='client_image')
    adhaar_front = models.ImageField(upload_to='adhaar_front')
    adhaar_back = models.ImageField(upload_to='adhaar_back')
    signature = models.ImageField(upload_to='signature',default='demo.png')
    is_deleted = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
    txn = models.CharField(max_length=20,default=0)
    registration_no = models.CharField(max_length=20,default=0)

    class Meta:
        managed = True
        db_table = 'customer_data'

    def __str__(self):
        return self.name

@receiver(models.signals.post_delete, sender=CustomerData)
def delete_files(sender, instance, *args, **kwargs):
    """ Deletes image files on `post_delete` """
    if instance.client_photo:
        _delete_file(instance.client_photo.path)
    if instance.adhaar_front:
        _delete_file(instance.adhaar_front.path)
    if instance.adhaar_back:
        _delete_file(instance.adhaar_back.path)
    if instance.signature:
        _delete_file(instance.signature.path)
 
class Receipt(models.Model):
    registration_no = models.CharField(max_length=20,default=0)
    receipt = models.ImageField(upload_to='receipt')
    is_deleted = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'receipt'
    
    def __str__(self):
        return self.registration_no

@receiver(models.signals.post_delete, sender=Receipt)
def delete_file(sender, instance, *args, **kwargs):
    """ Deletes thumbnail files on `post_delete` """
    if instance.receipt:
        _delete_file(instance.receipt.path)

class Certificate(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    father_name = models.CharField(max_length=255,null=True,blank=True)
    mother_name = models.CharField(max_length=255,null=True,blank=True)
    mobile = models.CharField(max_length=15,null=True,blank=True)
    client_photo = models.ImageField(upload_to='client_image')
    adhaar_front = models.ImageField(upload_to='adhaar_front')
    adhaar_back = models.ImageField(upload_to='adhaar_back')
    txn = models.CharField(max_length=20,default=0)
    service = models.CharField(max_length=255,default='No service')
    date = models.DateTimeField(auto_now=True)
    is_deleted = models.IntegerField(default=0)
    registration_no = models.CharField(max_length=20,default=0)
    
    class Meta:
        managed = True
        db_table = 'certificate'

@receiver(models.signals.post_delete, sender=Certificate)
def delete_certificate_files(sender, instance, *args, **kwargs):
    """ Deletes thumbnail files on `post_delete` """
    if instance.client_photo:
        _delete_file(instance.client_photo.path)
    if instance.adhaar_front:
        _delete_file(instance.adhaar_front.path)
    if instance.adhaar_back:
        _delete_file(instance.adhaar_back.path)

class UploadedCertificate(models.Model):
    registration_no = models.CharField(max_length=20,default=0)
    certificate = models.ImageField(upload_to='certificate')
    is_deleted = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'uploaded_certificate'

@receiver(models.signals.post_delete, sender=UploadedCertificate)
def delete_certificate(sender, instance, *args, **kwargs):
    """ Deletes thumbnail files on `post_delete` """
    if instance.certificate:
        _delete_file(instance.certificate.path)




