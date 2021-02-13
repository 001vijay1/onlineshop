from django import forms


class DownloadReceiptForm(forms.Form):
    registration_no = forms.CharField(label='REGISTRATION NO',help_text='Hints : SNPRXXXXXX',max_length=255,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))

    def clean_registration_no(self):
        registration_no = self.cleaned_data['registration_no']
        if len(registration_no)<10 or len(registration_no)>10:
            raise forms.ValidationError('Invalid registration number!')
        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return registration_no


class UploadReceiptForm(forms.Form):
    registration_no = forms.CharField(label='REGISTRATION NO',help_text='Hints : SNPRXXXXXX',max_length=255,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    receipt = forms.FileField(label='SELECT RECEIPT',required=True,widget=forms.ClearableFileInput(attrs={'class':'form-control','multiple': False}))

    def clean_registration_no(self):
        registration_no = self.cleaned_data['registration_no']
        if len(registration_no)<10 or len(registration_no)>10:
            raise forms.ValidationError('Invalid registration number!')
        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return registration_no