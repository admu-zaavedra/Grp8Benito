from django.shortcuts import redirect, render
from django.http import HttpResponse

from .forms import AccountForm, OrganizerAccountForm
from .models import Account

# Create your views here.
# def index(request):
#     return HttpResponse('Hello World! This came from the index view')


def register_view(request):
    if request.method == 'POST':
        if 'form1_submit' in request.POST:
            form1 = AccountForm(request.POST)
            form2 = OrganizerAccountForm()
            if form1.is_valid():
                form1.save()
                return redirect('/log_in/')
        elif 'form2_submit' in request.POST:
            form2 = OrganizerAccountForm(request.POST)
            form1 = AccountForm()
            if form2.is_valid():
                form2.save()
                return redirect('/log_in/')
    else:
        form1 = AccountForm()
        form2 = OrganizerAccountForm()
    return render(request, 'register/register.html', {'form1': form1, 'form2': form2})
