from django.db import models
from django.forms import ModelForm
from project.settings import DATE_INPUT_FORMATS

TIME_CHOICES=[
    ('10-11', '10-11'),
    ('11-12', '11-12'),
    ('12-13', '12-13'),
    ('13-14', '13-14'),
    ('14-15', '14-15'),
]

# Create your models here.
class AppointmentSchedule(models.Model):
    email = models.EmailField()
    name=models.CharField(max_length=50)
    contact_no = models.CharField(max_length=20)
    date = models.DateField()
    time= models.CharField(max_length=5, default="", choices= TIME_CHOICES)
