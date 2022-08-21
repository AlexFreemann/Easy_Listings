from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,PasswordResetForm,SetPasswordForm
#

class CreateUserForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user




class LoginForm(forms.Form):
    username = forms.CharField(label='Login',widget=forms.TextInput(attrs={'class': 'form-control', }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', }))



class ChangePassword(PasswordChangeForm):

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class ForgotPassword(PasswordResetForm):

    class Meta:
        model = User
        fields = ('email')


class SetNewPassword(SetPasswordForm):

    class Meta:
        model = User
        fields = '__all__'