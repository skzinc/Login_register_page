from django.db import models

# Create your models here.
class Myuser(models.Model):
    phone_no = models.CharField(max_length=12)

