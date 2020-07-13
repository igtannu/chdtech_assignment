from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator


# Create your models here.
class Destination(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    age = models.IntegerField(max_length=3,validators=[MinLengthValidator(2)])
    # age=models.IntegerField()
    

