from django import forms


class CampaignForm(forms.Form):
  name = forms.CharField(required=True)
  budget = forms.IntegerField()
  purpose = forms.CharField(widget=forms.TextInput())
