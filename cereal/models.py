from django.db import models
from user.models import Profile
from django.db.models import JSONField
# Create your models here.


# Model for product categories
class ProductCategory(models.Model):
    category = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


# Model for products
class ProductModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=2500)
    price = models.FloatField()
    rating = models.FloatField()
    category = models.ManyToManyField(ProductCategory, related_name='products')
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    manufacturer = models.CharField(max_length=56, default='Satan')

    # Functions to filter products by category
    @staticmethod
    def get_by_category(category_name):
        category_id = ProductCategory.objects.get(category_name=category_name).category
        products = ProductModel.objects.raw("SELECT * FROM cereal_productmodel P \
                                             inner join cereal_productmodel_category PC\
                                             on P.id = PC.productmodel_id\
                                             where PC.productcategory_id = {}".format(category_id))
        return products

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        return str(self.price) + ' ISK '

    def get_stock(self):
        return self.stock

    def get_rating(self):
        return self.rating

    def get_manufacturer(self):
        return self.manufacturer

    def create(self, name, description, price, manufacturer):
        new = ProductModel()
        new.name = name
        new.description = description
        new.price = price
        new.rating = 0
        new.manufacturer = manufacturer
        new.save()
        return new

    def update_name(self, name):
        self.name = name
        self.save()
        return self

    def update_description(self, description):
        self.description = description
        self.save()
        return self

    def update_price(self, price):
        self.price = price
        self.save()
        return self

    def update_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer
        self.save()
        return self

    def __str__(self):
        '''Returns a stringed version of product instance formatted like this: Product 9999.kr'''
        return "{} {}".format(self.name, self.get_price())


# Model for orders
# Used for order history functionality of the page
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    items = JSONField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time', '-id']

    def __str__(self):
        return "User {}, items {}".format(self.user, self.items)