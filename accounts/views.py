from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from .forms import SignUpForm

# Create your views here.
def signup_view(request):

    #GET 요청 시 HTML 응답
    if request.method =='GET':
        form = SignUpForm
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)

    #POST 요청 시 데이터 생성
    else :
        form = SignUpForm(request.POST)

        if form.is_valid():
            #회원가입 처리
            instance = form.save()
            return redirect('index')
        else:
            return redirect('accounts:signup')

def login_view(request):
    #GET, POST 분리
    if request.method =='GET':
        return render(request, 'accounts/login.html', {'form' : AuthenticationForm()})
    else:
        form = AuthenticationForm(request, data = request.POST) #공식문서 인자 입력 참고
        #데이터 유효성 검사
        if form.is_valid():
            #비지니스 로직 처리 - 로그인 성공
            login(request, form.user_cache)
            #응답
            return redirect('index')
        else:
            #비지니스 로직 처리 - 로그인 실패
            #응답
            return render(request, 'accounts/login.html', {'form' : form})
    
def logout_view(request):
    #데이터 유효성 검사
    if request.user.is_authenticated:
        #비지니스 로직 처리 - 로그 아웃
        logout(request)
    #응답
    return redirect('index')
    