from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets
from user.models import Profile, LocationsModel
from django import forms

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(required=True, label="First name")
    last_name = forms.CharField(required=True, label="Last name")
    profile_image = forms.ImageField(required=False, label="Profile image")
    street_name = forms.CharField(required=True, label="Street name")
    house_number = forms.CharField(required=True, label="House number")
    country = forms.ModelChoiceField(LocationsModel.objects.all(), required=True, label="Country")
    zipcode = forms.IntegerField(required=True, label="Zip")
    city = forms.CharField(required=True, label="City")
    class Meta:
        model = User
        fields = [
                  "username", "email", "password1", "password2",
                  "profile_image", "first_name", "last_name"
                ]


class ProfileForm(ModelForm):
    profile_image = forms.ImageField(required=False, label="Profile image")
    card_holder = forms.CharField(required=False, label="Card holder")
    card_number = forms.IntegerField(required=False, label="Card number")
    card_expiration = forms.DateField(required=False, widget=widgets.SelectDateWidget(attrs={'class': 'form-control'}), label="Card expiration")
    street_name = forms.CharField(required=False, label="Street name")
    house_number = forms.CharField(required=False, label="House Number")
    city = forms.CharField(required=False, label="City")
    zipcode = forms.IntegerField(required=False, label="Zip")

    class Meta:
        model = Profile
        exclude = ['id', 'user', 'card_cvc']
        widgets = {
            'profile-image': widgets.TextInput(attrs={'class': 'form-control'}),
        }
