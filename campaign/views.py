from django.shortcuts import render

# Create your views here.


def campaign_list(request):
      return render(request, 'campaign/index.html', {})
