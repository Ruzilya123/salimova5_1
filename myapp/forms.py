from django import forms

NAME_WIDGET = {
    'class': 'form_item',
    'placeholder': 'Имя'
}

EMAIL_WIDGET = {
    'class': 'form_item',
    'placeholder': 'ivanov@mail.ru'
}

PASSWORD_WIDGET = {
    'class': 'form_item',
    'placeholder': '****'
}




class Login(forms.Form):
    name = forms.CharField(label='Имя', max_length=100, required=True,
                           widget=forms.TextInput(attrs=NAME_WIDGET))
    password = forms.CharField(label='Пароль', max_length=100, required=True,
                               widget=forms.PasswordInput(attrs=PASSWORD_WIDGET))


class Register(Login):
    name = forms.CharField(label='Имя', max_length=100, required=True,
                           widget=forms.TextInput(attrs=NAME_WIDGET))
    email = forms.EmailField(label='Почта', max_length=100, required=True,
                             widget=forms.EmailInput(attrs=EMAIL_WIDGET))
    password = forms.CharField(label='Пароль', max_length=100, required=True,
                               widget=forms.PasswordInput(attrs=PASSWORD_WIDGET))
