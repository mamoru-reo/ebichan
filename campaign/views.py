from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from .models import Campaign
from .forms import CampaignForm

# Create your views here.


def campaign_list(request):
	campaigns = Campaign.objects.all()
	page_obj = paginate_queryset(request, campaigns, 5)
	return render(request, 'campaign/index.html', {
		'campaigns':page_obj.object_list,
		'paginator':page_obj
	})

def paginate_queryset(request, queryset, count):
	paginator = Paginator(queryset, count)
	page = request.GET.get('page')
	try:
		page_obj = paginator.page(page)
	except PageNotAnInteger:
		page_obj = paginator.page(1)
	except EmptyPage:
		page_obj = paginator.page(paginator.num_pages)
	return page_obj




def campaign_form(request):
	post_data = request.POST
	#post_data['campany_id'] = [request.user.campany_id]
	form = CampaignForm(post_data or None, initial={'campany_id':request.user.campany_id})
	#print(form)
	
	if form.is_valid():
		Campaign.objects.create(**form.cleaned_data)
		return redirect('campaign_list')
	
	return render(request, 'campaign/form.html', {'form':form})


def campaign_group(request):
	return render(request, 'campaign/group_list.html', {})


def material_upload(request):
	return render(request, 'campaign/material_upload.html')
