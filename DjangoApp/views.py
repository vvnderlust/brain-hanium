from django.shortcuts import render,redirect
from django.conf import settings

def home(request):
    # 홈페이지 뷰 로직
    if settings.IS_NOW_LOGIN: #true일 경우
        return redirect('patient:list')
        print("login completed!")
    else:
        return redirect('common:login')
        print("not login")



