
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('commercial', 'Commercial'),
        ('client', 'Client'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')
    telephone = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username