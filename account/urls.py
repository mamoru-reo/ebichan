from django.urls import path
from . import views


urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('logout', views.Logout.as_view(), name='logout'),
    path('registration', views.registration_user, name='registration'),
    path('api_tk2', views.api_tk2, name='api_tk2'),

]
