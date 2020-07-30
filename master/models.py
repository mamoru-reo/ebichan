from django.db import models
from django.utils import timezone


# Create your models here.

class Material_type(models.Model):
  name = models.CharField(max_length=50)
  snum = models.IntegerField()
  created = models.DateTimeField(default=timezone.now)
  modified = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.modified = timezone.now()
    self.save()


class Material_role(models.Model):
  name = models.CharField(max_length=50)
  snum = models.IntegerField()
  created = models.DateTimeField(default=timezone.now)
  modified = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.modified = timezone.now()
    self.save()


class Font_item(models.Model):
  path = models.TextField()
  name = models.CharField(max_length=50)
  snum = models.IntegerField()
  created = models.DateTimeField(default=timezone.now)
  modified = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.modified = timezone.now()
    self.save()


class Movie_template(models.Model):
  name = models.CharField(max_length=50)
  config_jd = models.TextField()
  created = models.DateTimeField(default=timezone.now)
  modified = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.modified = timezone.now()
    self.save()


class Ads_status(models.Model):
  name = models.CharField(max_length=50)
  snum = models.IntegerField()
  created = models.DateTimeField(default=timezone.now)
  modified = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.modified = timezone.now()
    self.save()


class Material_choose_type(models.Model):
  name = models.CharField(max_length=50)
  snum = models.IntegerField()
  created = models.DateTimeField(default=timezone.now)
  modified = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.modified = timezone.now()
    self.save()




def __str__(self):
  return self.name
