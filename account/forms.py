from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(forms.Form):
  company_name = forms.CharField(widget=forms.TextInput(
      attrs={'placeholder': '会社名・組織名'}))
  username = forms.CharField(widget=forms.TextInput(
      attrs={'placeholder': 'ユーザネーム'}))
  address = forms.CharField(max_length=8, widget=forms.TextInput(
      attrs={'placeholder': '郵便番号(「-」ハイフン含)', 'class': 'p-postal-code', 'size': '8', 'maxlength': '8', 'required': "required"})
  )
  pref = forms.CharField(max_length=40, widget=forms.TextInput(
      attrs={'placeholder': '都道府県', 'class': 'p-region', 'required': "required"})
  )
  city = forms.CharField(max_length=40, widget=forms.TextInput(
      attrs={'placeholder': '住所１', 'class': 'p-locality', 'required': "required"})
  )
  city2 = forms.CharField(max_length=40, widget=forms.TextInput(
      attrs={'placeholder': '住所２(番地・マンション名)', 'class': 'p-street-address', 'required': "required"})
  )
  tell = forms.RegexField(regex=r'^\d{2,4}-\d{2,4}-\d{4}$', widget=forms.TextInput(
      attrs={'placeholder': '電話番号(「-」ハイフン含)'}))
  email = forms.EmailField(label="メールアドレス", widget=forms.EmailInput(
      attrs={'placeholder': 'メールアドレス', 'required': "required"}))
  password = forms.CharField(
      widget=forms.PasswordInput(attrs={'placeholder': 'パスワード', 'required': "required"}))
  password2 = forms.CharField(
      widget=forms.PasswordInput(attrs={'placeholder': 'パスワード再確認', 'required': "required"}))


class LoginForm(AuthenticationForm):
  """ログオンフォーム"""

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in self.fields.values():
      field.widget.attrs['class'] = 'form-control'
      field.widget.attrs['placeholder'] = field.label


#TiktokのAPI連携設定フォーム
class Tk2appcdForm(forms.Form):
	tk2_app_cd = forms.CharField(widget=forms.TextInput(
		attrs={'placeholder': 'コピー＆ペーストしてください'}))
	tk2_app_sec = forms.CharField(widget=forms.TextInput(
		attrs={'placeholder': 'コピー＆ペーストしてください'}))
	
	
