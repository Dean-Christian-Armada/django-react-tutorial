from django.db import models

# import datetime

# Create your models here.
class Band(models.Model):
	name = models.CharField(max_length=128, unique=True)
	bio = models.TextField(null=True, blank=True)
	image = models.CharField(max_length=255, unique=True)
	date_added = models.DateField(auto_now_add=True)