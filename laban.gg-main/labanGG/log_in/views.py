from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

from .forms import LogInForm
# Create your views here.

def log_in_view(request):
    user = request.user
    if (user):
        logout(request)

    if request.method == 'POST':
        if 'form_submit' in request.POST:
            form = LogInForm(request.POST)
            if form.is_valid():
                email_username = form.cleaned_data['email_username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=email_username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/games/')
    else:
        form = LogInForm()
    return render(request, 'log_in/log_in.html', {'form': form})