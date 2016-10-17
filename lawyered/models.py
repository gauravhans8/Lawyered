from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class person(models.Model):
	name = models.CharField(max_length=250)
	area = models.CharField(max_length=250)
	specialization = models.CharField(max_length=250)
	details = models.TextField()
	image = models.ImageField(upload_to='lawyered/media/',blank=True)
def __str__(self):
	return self.title	
	
# Create your models here.
