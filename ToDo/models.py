from email import contentmanager
from django.db import models

# Create your models here.
class ToDo(models.Model):
    content = models.TextField()

