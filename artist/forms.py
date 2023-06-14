from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .enums import GenderChoice
from .models import Artist, Music, UserArtist


class CreateUserArtistForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=100,
        required=True,
        help_text='Enter First Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
    )
    last_name = forms.CharField(
        max_length=100,
        required=True,
        help_text='Enter Last Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
    )

    username = forms.CharField(
        max_length=200,
        required=True,
        help_text='Enter Username',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
    )

    email = forms.EmailField(
        max_length=100,
        required=True,
        help_text='Enter Email Address',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
    )
    password1 = forms.CharField(
        help_text='Enter Password',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        required=True,
        help_text='Enter Password Again',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),
    )

    phone_number = forms.IntegerField(
        help_text='Enter Phone Number',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
    )
    date_of_birth = forms.DateTimeField(
        required=True,
        help_text='Date of Birth',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth'}),
    )
    gender = forms.ChoiceField(
        required=True,
        help_text='Gender',
        choices=[(gender.value, gender.name) for gender in GenderChoice]
        # widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Gender'}),
    )
    address = forms.CharField(
        max_length=100,
        required=True,
        help_text='Enter Address',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Address'}),
    )

    class Meta:
        model = UserArtist
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "phone_number",
            "date_of_birth",
            "gender",
            "address"
        ]


class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'
        exclude = ['created_at', 'updated_at']


class MusicForm(ModelForm):
    class Meta:
        model = Music
        fields = '__all__'
        exclude = ['created_at', 'updated_at']
