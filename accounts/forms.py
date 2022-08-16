from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model


class CustomUSerCreationForm(UserCreationForm):
    model = get_user_model()
    fields = ('email', 'username',)


class CustomUserChangeForm(UserChangeForm):
    model = get_user_model()
    fields = ('email', 'username',)

