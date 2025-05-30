from django import forms

from .models import Account, OrganizerAccount

class AccountForm(forms.ModelForm):
    confirm_email = forms.EmailField(max_length=100)
    confirm_password = forms.CharField(max_length=32)
    class Meta:
        model = Account
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super(AccountForm, self).clean()
        email = cleaned_data.get("email")
        confirm_email = cleaned_data.get("confirm_email")
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if email != confirm_email:
            self.add_error('confirm_email', "Email does not match")

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match")

        return cleaned_data
    
class OrganizerAccountForm(forms.ModelForm):
    confirm_email = forms.EmailField(max_length=100)
    confirm_password = forms.CharField(max_length=32)
    class Meta:
        model = OrganizerAccount
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'contact_number', 'past_experience', 'additional_comments']

        def clean(self):
            cleaned_data = super(AccountForm, self).clean()
            email = cleaned_data.get("email")
            confirm_email = cleaned_data.get("confirm_email")
            password = cleaned_data.get("password")
            confirm_password = cleaned_data.get("confirm_password")

            if email != confirm_email:
                self.add_error('confirm_email', "Email does not match")

            if password != confirm_password:
                self.add_error('confirm_password', "Password does not match")

            return cleaned_data


    
        

