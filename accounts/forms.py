from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)


class CustomUserCreationForm(UserCreationForm):
    
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder': '사용자 이름',

        }),
        error_messages={
            'required': '다른 username을 입력해주세요'
        }
    )

    email  = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder': '사용자 email',

        }),
        error_messages={
            'required': '다른 email을 입력해주세요'
        }
    )

    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'비밀번호(8자 이상)'

        }),
        error_messages={
            'required': '비밀번호를 확인해주세요.'
        }
    )

    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'비밀번호 확인'

        }),
        error_messages={
            'required': '비밀번호를 확인해주세요.'
        }
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email',)