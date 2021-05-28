from django.forms import ModelForm, widgets
from user.models import Profile

class ShippingForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            "first_name",
            "last_name",
            "email",
            "street_name",
            "house_number",
            "location_id",
            "city",
            "zipcode",
        ]
        exclude = ['id', 'user', 'favorite_cereal', 'profile-image']


class PaymentForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            "card_holder",
            "card_number",
            "card_expiration",
            "card_cvc",
        ]
        labels = {
            "card_holder": 'Name on card',
            "card_number": 'Card number',
            "card_expiration": 'Expiration',
            'card_cvc': 'CVC',
        }
        widgets = {
            'card_expiration': widgets.SelectDateWidget(),
            'card_cvc': widgets.TextInput(attrs={'class': 'soc-input_cvc'}),
        }
