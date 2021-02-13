from django import forms



class PanOnlineForm(forms.Form):
    CHOICES = [('Male','Male'),('Female','Female')]
    name = forms.CharField(label='NAME',max_length=255,required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Full Name'}))
    father_name = forms.CharField(label='FATHER NAME',max_length=255,required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Your Father's Name"}))
    dob = forms.DateField(label='DOB',required=True,input_formats=['%d/%m/%Y'],widget=forms.TextInput(attrs={'class':'form-control','placeholder':'DD/MM/YYYY'}))
    gender = forms.ChoiceField(label='GENDER',choices=CHOICES,widget=forms.Select(attrs={'class':'form-control'}),initial=CHOICES[0])
    mobile_no = forms.CharField(label='MOBILE NO',required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Mobile'}))
    email = forms.EmailField(label='EMAIL',max_length=255,required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}))
    address = forms.CharField(label='ADDRESS',max_length=255,required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Address'}))
    photo = forms.FileField(required=True,widget=forms.ClearableFileInput(attrs={'class':'form-control','multiple': False}), label="UPLOAD PHOTO")
    adhaar_front = forms.FileField(required=True,widget=forms.ClearableFileInput(attrs={'class':'form-control','multiple': False}), label="UPLOAD ADHAAR FRONT PHOTO")
    adhaar_back = forms.FileField(required=True,widget=forms.ClearableFileInput(attrs={'class':'form-control','multiple': False}), label="UPLOAD ADHAAR BACK PHOTO")
    signature = forms.FileField(required=True,widget=forms.ClearableFileInput(attrs={'class':'form-control','multiple': False}), label="UPLOAD SIGNATURE OR THUMB")

    
    def clean_mobile_no(self):
        mobile_no = self.cleaned_data['mobile_no']
        if len(mobile_no)<10 or len(mobile_no)>10:
            raise forms.ValidationError('Mobile no should be 10 digit!')
        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return mobile_no

class TransactionForm(forms.Form):
    transaction_id = forms.CharField(label='TRANSACTION ID',max_length=15,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))

    def clean_transaction_id(self):
        transaction_id = self.cleaned_data['transaction_id']
        if len(transaction_id)<8 or len(transaction_id)>15:
            raise forms.ValidationError('Invalid?')
        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return transaction_id
