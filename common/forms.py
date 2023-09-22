from django import forms
from django.contrib.auth.hashers import check_password, make_password # 비밀번호 저장시 make_password이용(hash값)
from .models import CustomUser as User

class CustomUserForm(forms.ModelForm):
    # hospital 필드를 ChoiceField로 정의
    hospital = forms.ChoiceField(choices=User.HOSPITAL_CHOICES,
                                 widget=forms.Select(attrs={'class': 'custom-select'}))
    class Meta:
        model = User
        fields = ['username', 'password', 'hospital']

class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required': '아이디를 입력하세요'
        },
        max_length=20,
        label='아이디',
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력하세요'
        },
        widget=forms.PasswordInput,
        label='비밀번호'
    )

    def clean(self):  # validation을 진행하는 메서드
        cleaned_data = super().clean()  # 부모 클래스에서 갖고 있던 clean을 상속 받아요.
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if password and username:  # 비밀번호 입력란 2개가 입력되어야하고
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                self.add_error('username', '해당 아이디가 없습니다.')
                return
            if not password == user.password:  # 좌항은 사용자 입력값, 우항은 db에 있는값(hash값으로 저장된 비밀번호) 둘을 서로 비교해줘요.
                self.add_error('password', '비밀번호가 틀렸습니다.')

            else: #로그인이 진행되는 경우
                self.username = user.username  # db에서 가져온 정보를 username에 할당
                user.is_login=True
                user.save()
                print(user.is_login)


