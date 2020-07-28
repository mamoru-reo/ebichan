from django.shortcuts import render

# Create your views here.


def campaign_list(request):
  return render(request, 'campaign/index.html', {})


def campaign_form(request):
  return render(request, 'campaign/form.html', {})


def campaign_group(request):
  return render(request, 'campaign/group_list.html', {})


def material_upload(request):
  return render(request, 'campaign/material_upload.html')
