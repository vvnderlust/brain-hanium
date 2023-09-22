from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    #patient_img = models.ImageField()
    latest_diagnosis = models.DateField()
    birthday = models.DateField()
    patient_num = models.IntegerField()
    def __str__(self):
        return f"{self.last_name}, {self.first_name}, {self.patient_num}"
    
