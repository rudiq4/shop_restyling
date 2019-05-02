from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Логін'
        self.fields['password'].label = 'Пароль'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError('Користувача з таким іменем не існує, спробуйте ще раз!')
        user = User.objects.get(username=username)
        if not user.check_password(password):  # check_password -> bool(0/1)
            raise forms.ValidationError('Пароль вказано не вірно')


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_check = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'password_check', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = '*Допускаєься: 150 або менше символів. тільки букви, цифри та знаки'
        self.fields['password'].label = 'Пароль'
        self.fields['password_check'].label = 'Повторіть пароль'

    def clean(self):  # Обработка исключений
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        # email = self.cleaned_data['email']
        password_check = self.cleaned_data['password_check']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Користувач з таким іменем вже зареєстрований')
        if password != password_check:
            raise forms.ValidationError('Паролі не співпадають')
