from django.db import models

# Create your models here.


class Patient(models.Model):
  fname = models.CharField(max_length=15)
  lname = models.CharField(max_length=15)
  DoB = models.DateTimeField(default=True)

class Meta:
      db_table = 'Patient'
