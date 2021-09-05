from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# Create your models here.

class jobInfo(models.Model):

    jobRole = models.CharField(max_length=256)
    jobDescription = models.CharField(max_length=10000)
    jobLocation = models.CharField(max_length=256)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phoneNumber = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    def __str__(self):
        return self.phoneNumber
