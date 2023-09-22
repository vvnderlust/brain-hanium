from django.urls import path
from . import views
from .views import ThankYouView,UserCreateView, UserListView, LoginView, LogoutView
from django.contrib.auth import views as auth_views

app_name = 'common'

urlpatterns= [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView, name='logout'),
    path('thank_you/', ThankYouView.as_view(), name='thank_you'),  # path는 Home_view를 함수로 예상함
    path('create_user/', UserCreateView.as_view(), name='create_user'),
    path('list_user/',UserListView.as_view(), name='list_user')
]