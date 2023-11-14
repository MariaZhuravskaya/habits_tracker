from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='почта', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='город', **NULLABLE)

