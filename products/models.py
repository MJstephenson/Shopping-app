from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class AlcoholType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    ALCOHOL_CHOICES = [
        ('Beer', 'Beer'),
        ('Wine', 'Wine'),
        ('Spirit', 'Spirit'),
    ]

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    alcohol_type = models.ForeignKey(
        'AlcoholType', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    new_arrival = models.BooleanField(
         default=False, help_text=
         "Check this if the product is a new arrival.")
    deal = models.BooleanField(default=False, help_text=
                               "Check this if the product is on deal.")
    clearance = models.BooleanField(
        default=False, help_text="Check this if the product is on clearance.")
    rating = models.DecimalField(
         max_digits=6, decimal_places=1, null=True, blank=True)
    alcohol_content = models.DecimalField(
        max_digits=4, decimal_places=1, help_text=
        "Alcohol content in percentage")
    volume = models.DecimalField(
        max_digits=5, decimal_places=0, help_text="Volume in ml")
    country_of_origin = models.CharField(max_length=100)
    year_of_production = models.PositiveIntegerField(null=True, blank=True)
    taste_notes = models.TextField(max_length=200, null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
