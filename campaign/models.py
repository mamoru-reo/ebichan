from django.db import models
from django.utils import timezone
from account.models import Campany
from master.models import Movie_template, Ads_status, Ads_group_status
import uuid

# Create your models here.


class Campaign(models.Model):
  name = models.TextField(blank=True)  #キャンペーン名
  budget = models.IntegerField(blank=True, null=True)  # 予算
  purpose = models.TextField(blank=True, null=True)  # 目的
  created = models.DateTimeField(default=timezone.now)
  modified = models.DateTimeField(blank=True, null=True)
  campany = models.ForeignKey(
      Campany, on_delete=models.CASCADE, related_name='campaign'
  )

  def publish(self):
    self.modified = timezone.now()
    self.save()


class Ads_group(models.Model):
  name = models.CharField(max_length=50)
  colors_jd = models.TextField()
  stream_dt = models.DateField(blank=True, null=True)  # 配信日
  nonstream_dt = models.DateField(blank=True, null=True)  # 配信停止日
  created = models.DateTimeField(default=timezone.now)
  modified = models.DateTimeField(blank=True, null=True)
  ads_group_status = models.ForeignKey(
    Ads_group_status, on_delete=models.CASCADE, related_name='ads_group'
  )
  campaign = models.ForeignKey(
      Campaign, on_delete=models.CASCADE, related_name='ads_group'
  )

  def publish(self):
    self.modified = timezone.now()
    self.save()


class Ads_item(models.Model):
  id = models.UUIDField(
      primary_key=True, default=uuid.uuid4, editable=False)
  colors_jd = models.TextField()  # jsonで色を格納
  use_material_jd = models.TextField()  # 動画素材管理
  stream_dt = models.DateField(blank=True, null=True)  # 配信日
  nonstream_dt = models.DateField(blank=True, null=True)  # 配信停止日
  created = models.DateTimeField(default=timezone.now)
  modified = models.DateTimeField(blank=True, null=True)
  parent_ads_item_cd = models.TextField(blank=True, null=True) #派生元の広告データ
  ads_group = models.ForeignKey(
      Ads_group, related_name='ads_item', on_delete=models.CASCADE)
  movie_template = models.OneToOneField(
      Movie_template, related_name='ads_item', on_delete=models.CASCADE)
  ads_status = models.OneToOneField(
      Ads_status, related_name='ads_item', on_delete=models.CASCADE)

  def publish(self):
    self.modified = timezone.now()
    self.save()
