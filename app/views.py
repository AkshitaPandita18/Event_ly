from django.shortcuts import render, redirect
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from app.form import AppointmentScheduleForm
from app.models import AppointmentSchedule

# Create your views here.
def home(request):
    count= User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })

def signup(request):
    if request.method == 'POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form= UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })

def event(request):
    return render(request, 'event.html')

def details(request):
    r_form= AppointmentScheduleForm(request.POST)
    return render(request, 'details.html',{
        'form': r_form, 'redirected': False
    })

def send(request):
    if request.method== 'POST':
        r_form= AppointmentScheduleForm(request.POST)
        if r_form.is_valid():
            email = r_form.cleaned_data['email']
            name = r_form.cleaned_data['name']
            contact_no = r_form.cleaned_data['contact_no']
            date = r_form.cleaned_data['date']
            time = r_form.cleaned_data['time']
            r=AppointmentSchedule(email=email, name=name, contact_no=contact_no, date=date, time=time)
            r.save()
            return render(request, 'details.html', {
                'form': r_form, 'redirected': True
            })
    else:
        r_form= AppointmentScheduleForm()
    return render(request, 'details.html',{
        'form': r_form, 'redirected': False
    })
