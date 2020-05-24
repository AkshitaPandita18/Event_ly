from django import forms
from project.settings import DATE_INPUT_FORMATS
from app.models import TIME_CHOICES

class AppointmentScheduleForm(forms.Form):
    email = forms.EmailField(label='Email')
    name= forms.CharField(label='Name', max_length=50)
    contact_no = forms.CharField(label='Contact No', max_length=20)
    date = forms.DateField(label='Date', input_formats=DATE_INPUT_FORMATS)
    time= forms.CharField(label='Time',max_length=5, widget=forms.Select(choices=TIME_CHOICES))
