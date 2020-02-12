from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='service_picture')

    def __str__(self):
        return self.title


