from django.db import models
import string
import random

# Create your models here.


class ModelOne(models.Model):
    test = models.CharField(max_length=50, unique=True)
