from django.db import models
from django.utils import timezone
from account.models import Campany
from campaign.models import Ads_group, Ads_item
from master.models import Material_type, Material_role, Font_item
from master.models import Movie_template
import uuid

# Create your models here.


class Asset(models.Model):
  id = models.UUIDField(
      primary_key=True, default=uuid.uuid4, editable=False)
  file_name = models.ImageField(upload_to=None, blank=True, null=True)
  path_name = models.FileField(max_length=100)
  mine = models.TextField()
  created = models.DateTimeField(default=timezone.now)
  modified = models.DateTimeField(blank=True, null=True)
  campany = models.ForeignKey(
      Campany, on_delete=models.CASCADE, related_name='asset'
  )

  def publish(self):
    self.modified = timezone.now()
    self.save()


class Movie(models.Model):
  id = models.UUIDField(
      primary_key=True, default=uuid.uuid4, editable=False)
  movie_path = models.FileField(upload_to=None, max_length=100)  # 動画の保存先
  ver_num = models.IntegerField()  # 世代管理
  created = models.DateTimeField(default=timezone.now)
  modified = models.DateTimeField(blank=True, null=True)
  ads_item = models.OneToOneField(
      Ads_item, on_delete=models.CASCADE, related_name='movie'
  )
  movie_template = models.OneToOneField(
      Movie_template, on_delete=models.CASCADE, related_name='movie'
  )

  def publish(self):
    self.modified = timezone.now()
    self.save()


class Movie_material(models.Model):
  id = models.UUIDField(
      primary_key=True, default=uuid.uuid4, editable=False)
  deleted = models.BooleanField(null=True)
  created = models.DateTimeField(default=timezone.now)
  modified = models.DateTimeField(blank=True, null=True)
  ads_group = models.OneToOneField(
      Ads_group, related_name='movie_material', on_delete=models.CASCADE)
  asset = models.ForeignKey(
      Asset, on_delete=models.CASCADE, related_name='movie_material'
  )
  material_type = models.ForeignKey(
      Material_type, on_delete=models.CASCADE, related_name='movie_material'
  )
  material_role = models.ForeignKey(
      Material_role, on_delete=models.CASCADE, related_name='movie_material'
  )
  font_item = models.ForeignKey(
      Font_item, on_delete=models.CASCADE, related_name='movie_material'
  )

  def publish(self):
    self.modified = timezone.now()
    self.save()
