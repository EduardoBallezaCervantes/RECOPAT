from django.db import models

class Paciente(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
    def __str__(self):
        return self.name
    

# Create your models here.
class tessiu(models.Model):
    name=models.CharField(max_length=50)
    temperature = models.FloatField()
    color = models.FloatField()
    inflammation = models.FloatField()
   