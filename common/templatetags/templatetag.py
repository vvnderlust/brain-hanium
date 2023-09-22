from django import template
from ..models import CustomUser
from django.conf import settings
register = template.Library()

@register.simple_tag
def is_user_logged_in():
    global_login_user = settings.GLOBAL_LOGIN_USER #로그인한 유저의 이름을 받아옴

    if global_login_user == "NONE": #맨 처음 호출될 경우
        is_login = False
        pass
    else:
        #global로 방금 로그인한 유저의 is_login정보를 받아옴
        user = CustomUser.objects.get(username=global_login_user)
        is_login = user.is_login

    return is_login

