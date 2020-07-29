from django.urls import path
from . import views

urlpatterns = [
    path('campaign_list', views.campaign_list, name="campaign_list"),
    path('campaign_form', views.campaign_form, name="campaign_form"),
    path('campaign_update/<int:pk>', views.campaign_update, name="campaign_update"),
    path('campaign_group', views.campaign_group, name="campaign_group"),
    path('material_upload', views.material_upload, name="material_upload"),
]
