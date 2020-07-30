from django.urls import path
from . import views

urlpatterns = [
    path('campaign_list', views.campaign_list, name="campaign_list"),
    path('campaign_form', views.campaign_form, name="campaign_form"),
    path('campaign_update/<int:pk>', views.campaign_update, name="campaign_update"),
    path('campaign_delete/<int:pk>', views.campaign_delete, name="campaign_delete"),
    path('campaign_group', views.campaign_group, name="campaign_group"),
]
