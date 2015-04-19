from django.db import models
from django.utils import timezone

# Create your models here.

class Cat(models.Model):
  name = models.CharField(max_length=200)
  age = models.IntegerField()
  color = models.CharField(max_length=200)
  desc = models.TextField()
  adopted = models.DateTimeField( blank=True, null=True )
  fluffy = models.BooleanField()
  image = models.CharField(max_length=500, blank=True)

  def adopt(self):
    self.adopted = timezone.now()
    self.save()

  def __str__(self):
    return self.name
