from django.db import models

# Create your models here.
class Client(models.Model):
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]

    address = models.TextField()
    cell_phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.email} - {self.gender}"
