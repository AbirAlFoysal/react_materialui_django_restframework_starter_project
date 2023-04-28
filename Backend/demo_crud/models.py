from django.db import models

# Create your models here.

class Crud(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=100)
    def __str__(self):
        return self.text 