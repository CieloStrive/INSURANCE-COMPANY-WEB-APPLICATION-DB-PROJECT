from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.hashers import make_password
import wds.models as models


# 为了能注册，view这里就要接受到两种request，进入网页的GET，提交注册建立账户的POST
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        username = request.POST['username']  # 以字典形式提交的数据被获取
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        try:
            User.objects.get(username=username)  # 如果成功，要告诉用户有重复名
            return render(request, 'signup.html', {'check1': 'Username already exist'})
        except User.DoesNotExist:
            if password1 == password2:
                user = User.objects.create_user(username=username, password=password1)
                user.password = make_password(password1)  # 明文密码经过加密处理
                print('Encoded password:', make_password(password1))
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                user.save()
                messages.success(request, f'Your account has been created! You are now able to log in')
                return redirect('home_page')
            else:
                return render(request, 'signup.html', {'check2': 'Two passwords do not match'})
        # 如果用import的user的方法能查到同名这条，证明用户名重复，不存在会报错，我们不能让它报错，用try，


def signup_success(request):
    return render(request, 'signup_success.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST['username']  # 以字典形式提交的数据被获取
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)  # 去查有没有这个用户
        if user is None:
            return render(request, 'login.html', {'check': 'Username or password incorrect' })
        else:
            auth.login(request, user)
            current_user = request.user
            print(models.HomeInsurance.objects.filter(insurance_id='1100000153'))
            return redirect('home_page')


def logout(request):  # 登出不存在GET方法
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home_page')