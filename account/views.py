from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import(LoginView, LogoutView, )
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegistrationForm, LoginForm, Tk2appcdForm
# ログインパスを通す場合に必要
from django.contrib.auth.decorators import login_required
from .models import Campany, User
import re


# Create your views here.


class Login(LoginView):
  """ログインページ"""
  form_class = LoginForm
  template_name = 'registration/login.html'


class Logout(LoginRequiredMixin, LogoutView):
  """ログアウトページ"""
  template_name = 'registration/login.html'



import re
#tiktokのAPI設定ページ
def api_tk2(request):
	company = Campany.objects.get(pk=request.user.campany_id)
	
	form = Tk2appcdForm(request.POST or None, initial={'tk2_app_cd':company.tk2_app_cd, 'tk2_app_sec':company.tk2_app_sec})
	if form.is_valid():
		company.tk2_app_cd = form.cleaned_data['tk2_app_cd']
		company.tk2_app_sec = form.cleaned_data['tk2_app_sec']
		company.save()
		return redirect('campaign_list')
	
	return render(request, 'user_settings/tk2.html', {'form':form})


def has_digit(text):
  if re.search("\d", text):
    return True
  return False

# 新規登録


def registration_user(request):
  if request.method == 'POST':
    registration_form = RegistrationForm(request.POST)
    print(request.POST)
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']
    address = request.POST.get('address')
    pref = request.POST.get('pref')
    city = request.POST.get('city')
    city2 = request.POST.get('city2')
    tell = request.POST.get('tell')

    # ユーザーネームのバリデート
    # ここでユーザーネームの情報を取得する
    if not re.match(r'^[0-9a-zA-Z]*$', username):
      username_err = "5~20字以内半角英数字で入力してください"
      registration_form = RegistrationForm(request.POST)
      return render(request, 'registration/registration.html', {'registration_form': registration_form, 'username_err': username_err})

    user_data = User.objects.filter(username=username)
    if user_data:
      username_err = "この名前のユーザーは既に存在しています"
      registration_form = RegistrationForm(request.POST)
      return render(request, 'registration/registration.html', {'registration_form': registration_form, 'username_err': username_err})

    if len(username) < 5 or len(username) > 20:
      username_err = "5~20字以内半角英数字で入力してください"
      registration_form = RegistrationForm(request.POST)
      return render(request, 'registration/registration.html', {'registration_form': registration_form, 'username_err': username_err})

    # アドレスのバリデート
    if not re.match(r'^\d{3}-\d{4}$', address):
      address_err = "郵便番号はXXX-XXXXの形式で入力してください"
      registration_form = RegistrationForm(request.POST)
      return render(request, 'registration/registration.html', {'registration_form': registration_form, 'address_err': address_err})

    # 都道府県のバリデート
    if len(pref) < 2 or len(pref) > 41:
      pref_err = "都道府県は40字以内で入力してください"
      registration_form = RegistrationForm(request.POST)
      return render(request, 'registration/registration.html', {'registration_form': registration_form, 'pref_err': pref_err})

    # 住所のバリデート
    if len(city) < 2 or len(city) > 41:
      city_err = "市区町村は40字以内で入力してください"
      registration_form = RegistrationForm(request.POST)
      return render(request, 'registration/registration.html', {'registration_form': registration_form, 'city_err': city_err})

    # 住所2のバリデート
    if len(city2) < 2 or len(city2) > 41:
      city2_err = "番地・マンション名は40字以内で入力してください"
      registration_form = RegistrationForm(request.POST)
      return render(request, 'registration/registration.html', {'registration_form': registration_form, 'city2_err': city2_err})

    # 電話番号のバリデート
    if not re.match(r'^\d{2,4}-\d{2,4}-\d{4}$', tell):
      tell_err = '電話番号はXXXX-XXXX-XXXXの形式で入力してください'
      registration_form = RegistrationForm(request.POST)
      return render(request, 'registration/registration.html', {'registration_form': registration_form, 'tell_err': tell_err})

    # メールアドレスのバリデート
    if not re.match(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", email):
      email_err = "メールアドレスの形式が違います"
      registration_form = RegistrationForm(request.POST)
      return render(request, 'registration/registration.html', {'registration_form': registration_form, 'email_err': email_err})

    # パスワードのバリデード
    if len(password) < 8:
      password_err = "パスワードは８文字以上で入力してください"
      registration_form = RegistrationForm(request.POST)
      return render(request, 'registration/registration.html', {'registration_form': registration_form, 'password_err': password_err})

    if not has_digit(password):
      password_err = "半角のアルファベット、数字で入力してください"
      return render(request, 'registration/registration.html', {'registration_form': registration_form, 'password_err': password_err})

    # パスワード再確認のバリデード
    if len(password2) < 8:
      password2_err = "パスワードは８文字以上で入力してください"
      return render(request, 'registration/registration.html', {'registration_form': registration_form, 'password2_err': password2_err})

    if not has_digit(password2):
      password2_err = "アルファベット、数字が含まれていません"
      return render(request, 'registration/registration.html', {'registration_form': registration_form, 'password2_err': password2_err})

    # Campany登録処理
    campany = Campany.objects.create(
        address=address + pref + city + city2, tell=request.POST.get('tell')
    )

    # ユーザー登録処理
    if campany.id:
      user = User.objects.create_user(
          username=request.POST['username'], password=password, email=request.POST['email'], campany_id=campany.id
      )
      # もしユーザー保存できたらログインにリダイレクト
      if user.id:
        return render(request, 'registration/login.html')
      # 保存できなかったら戻る
      else:
        # 保存したcampanyを削除
        campany.delete()
        registration_form = RegistrationForm()
        err = "登録に失敗しました。再度登録してください"
        return render(request, 'registration/registration.html', {'registration_form': registration_form, 'err': err})
    else:
      registration_form = RegistrationForm()
      err = "登録に失敗しました。再度登録してください"
      return render(request, 'registration/registration.html', {'registration_form': registration_form, 'err': err})
  else:
    registration_form = RegistrationForm()
  return render(request, 'registration/registration.html', {'registration_form': registration_form})
