# Django imports
from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_save
from django.db import models

# Django Rest-framework imports
from rest_framework.authtoken.models import Token


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    salary = models.IntegerField()

    def __str__(self):
        return self.name


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)