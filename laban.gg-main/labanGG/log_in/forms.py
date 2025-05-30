from django import forms

from register.models import Account

class LogInForm(forms.Form):
    email_username = forms.CharField(max_length=100, label="Email or username")
    password = forms.CharField(max_length=32)

    def clean(self):
        cleaned_data = super(LogInForm, self).clean()
        email_username = cleaned_data.get("email_username")
        password = cleaned_data.get("password")

        if Account.objects.filter(username=email_username).exists():
           if Account.objects.filter(password=password).exists():
              pass
           else:
               self.add_error('password', "Password is incorrect")
        elif Account.objects.filter(email=email_username).exists():
            if Account.objects.filter(password=password).exists():
              pass
            else:
               self.add_error('password', "Password is incorrect")
        else:
           self.add_error('email_username', "Email or username does not exist ")

        return cleaned_data