from django.db import models

# Create your models here.

class mama(models.Model):
    kitab = models.CharField(max_length=100)
    bab = models.CharField(max_length=50)
    fasol = models.CharField(max_length=50)
    penjelasan = models.IntegerField(null=True)

    def __str__(self):
        return self.kitab

