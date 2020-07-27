from django.urls import path
from . import views

urlpatterns = [
    path('campaign_list/', views.campaign_list, name="campaign_list"),
]
