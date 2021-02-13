from django import forms


class CertificateForm(forms.Form):
    name = forms.CharField(label='नाम',max_length=255,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    father_name = forms.CharField(label='पिता का नाम',max_length=255,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    mother_name = forms.CharField(label='माता का नाम',max_length=255,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    mobile_no = forms.CharField(label='मोबाइल नंबर',max_length=15,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    client_photo = forms.FileField(label='अपनी फोटो अपलोड करें',required=True,widget=forms.ClearableFileInput(attrs={'class':'form-control','multiple': False}))
    adhaar_front = forms.FileField(label='अधार फ्रंट फोटो अपलोड करें',required=True,widget=forms.ClearableFileInput(attrs={'class':'form-control','multiple': False}))
    adhaar_back = forms.FileField(label='अधार बैक फोटो अपलोड करें',required=True,widget=forms.ClearableFileInput(attrs={'class':'form-control','multiple': False}))

    def clean_mobile_no(self):
        mobile_no = self.cleaned_data['mobile_no']
        if len(mobile_no)<10 or len(mobile_no)>10:
            raise forms.ValidationError('Mobile no should be 10 digit!')
        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return mobile_no

class DownloadCertificateForm(forms.Form):
    registration_no = forms.CharField(label='REGISTRATION NO',help_text='Hints : SNCRXXXXXX',max_length=255,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))

    def clean_registration_no(self):
        registration_no = self.cleaned_data['registration_no']
        if len(registration_no)<10 or len(registration_no)>10:
            raise forms.ValidationError('Invalid registration number!')
        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return registration_no


class UploadCertificateForm(forms.Form):
    registration_no = forms.CharField(label='REGISTRATION NO',help_text='Hints : SNCRXXXXXX',max_length=255,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    certificate = forms.FileField(label='SELECT CERTIFICATE',required=True,widget=forms.ClearableFileInput(attrs={'class':'form-control','multiple': False}))

    def clean_registration_no(self):
        registration_no = self.cleaned_data['registration_no']
        if len(registration_no)<10 or len(registration_no)>10:
            raise forms.ValidationError('Invalid registration number!')
        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return registration_no