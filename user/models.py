from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.db import models


# Model for locations
class LocationsModel(models.Model):
    location_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=255, null=False)

    class Meta:
        ordering = ['country']

    def get_country(self):
        return self.country

    def __str__(self):
        return "{}".format(self.country)


""" Various validators"""


class NameValidator(RegexValidator):
    regex = '^[a-zA-ZÞÆÖþæöðáÁéÉíÍóÓúÚýÝ ]+$'
    message = "The name can only have English (and Icelandic) letters"
    code = 'invalid_name'


class CVCValidator(RegexValidator):
    regex = '^[0-9][0-9][0-9]$'
    message = "CVC is a three digit number"
    code = 'invalid_cvc'


class CCValidator(RegexValidator):
    regex = '(?:[0-9]{4}[-\s]){3}[0-9]{4}|[0-9]{16}'
    message = "Credit card number is a 16 digit number and is either consecutive or separated by dash or a single space"
    code = 'invalid_cc_number'


# Note: the none-class way to do validation
def validate_date(date):
    if date < timezone.now().date():
        raise ValidationError("Date cannot be in the past")


# Model for user Profiles
class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='users/', null=True)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email = models.EmailField(verbose_name='email address', max_length=255, null=False)
    street_name = models.CharField(max_length=255, null=False)
    house_number = models.CharField(max_length=25, null=False)
    card_holder = models.CharField(max_length=36, null=True, validators=[NameValidator()])
    card_number = models.CharField(max_length=19, null=True, validators=[CCValidator()])
    card_expiration = models.DateField(max_length=8, null=True, validators=[validate_date])
    card_cvc = models.IntegerField(null=True, validators=[CVCValidator()])
    location_id = models.ForeignKey(LocationsModel, verbose_name='Country', default=2, on_delete=models.DO_NOTHING)
    city = models.CharField(max_length=255, null=False)
    zipcode = models.IntegerField()

    def get_address(self):
        return "{}, {}, {}".format(self.street_name, self.house_number, self.zipcode)

    def get_customer(self):
        return self

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_email(self, email):
        self.email = email

    def set_street_name(self, street_name):
        self.street_name = street_name

    def set_house_number(self, house_number):
        self.house_number = house_number

    def set_zip(self, zipcode):
        self.zipcode = zipcode

    def set_city(self, city):
        self.city = city

    def set_country(self, country):
        self.location_id = LocationsModel.objects.get(location_id=country)
    
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


# Model for searches, used in order to store search history
class Searches(models.Model):
    query = models.CharField(max_length=999999)
    user = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    time = models.DateTimeField(auto_now_add=True)


