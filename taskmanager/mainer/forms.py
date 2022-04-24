from .models import *
from django.forms import *
from django import forms


# class InfoForm(ModelForm):
#       class Meta:
#         model = info
#         fields = ['name', 'surname', 'phone_num', 'email', 'password', 'genre']
#         widgets ={
#             "name": TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Жаңалық атауы'
#         }),
#             "surname": Textarea(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Жаңалықты енгізу'
#             }),
#             "phone_num": TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Жаңалық атауы'
#             }),
#             "city": TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Жаңалық атауы'
#         }),
#             "email": TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Жаңалық атауы'
#         }),
#             "password": TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Жаңалық атауы'
#         }),"genre": TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Жаңалық атауы'
#         }),
#       }

class AddPostForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Registration
        fields = '__all__'

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password']

    def clean_tel_number(self):
        tel_number = self.cleaned_data['tel_number']
        if tel_number<100000:
            raise ValidationError(' телефон номер 5-тен кіші болмау керек')
        return tel_number

