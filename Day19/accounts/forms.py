from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

#상속 : 기존에 있던 usercreation 에서 상속
class CustomUserCreationForm(UserCreationForm):
    # col 확장법
    address = forms.CharField(min_length=3)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('address', )


class CustomAuthenticationForm(AuthenticationForm):
    class Meta(AuthenticationForm):
        model = User