from django.db import models
from django.contrib.auth.models import AbstractUser, UnicodeUsernameValidator
from django.utils import timezone

# Create your models here.


class Campany(models.Model):
  tk2_app_cd = models.TextField()
  address = models.TextField()
  tell = models.TextField()
  email = models.EmailField()
  tk2_app_sec = models.TextField()
  created = models.DateTimeField(default=timezone.now)
  modified = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.modified = timezone.now()
    self.save()


class User(AbstractUser):
  email = models.EmailField()
  created = models.DateTimeField(default=timezone.now)
  modified = models.DateTimeField(blank=True, null=True)
  campany = models.ForeignKey(
      Campany, on_delete=models.CASCADE, related_name='user'
  )

  def publish(self):
    self.modified = timezone.now()
    self.save()

  EMAIL_FIELD = 'email'
  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = ['name']

  class Meta(AbstractUser.Meta):
    swappable = 'AUTH_USER_MODEL'
