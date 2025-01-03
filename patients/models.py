from django.db import models

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    birth_date = models.DateField()
    address = models.TextField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name