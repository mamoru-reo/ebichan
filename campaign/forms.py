from django import forms


class CampaignForm(forms.Form):
	name = forms.CharField(required=True)
	campany_id = forms.IntegerField(required=True, widget=forms.HiddenInput())
	#budget = forms.IntegerField(required=False)
	#purpose = forms.CharField(required=False, widget=forms.TextInput())
