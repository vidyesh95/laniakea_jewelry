from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    userid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    productid = models.IntegerField(primary_key=True)
    productname = models.CharField(max_length=100)
    type = (
        ("Earrings", "Earrings"),
        ("Cocktail Ring", "Cocktail Ring"),
        ("Necklace", "Necklace"),
        ("Bangle", "Bangle"),
        ("Mangal Sutra", "Mangal Sutra"),
        ("Chain", "Chain"),
        ("Engagement Ring", "Engagement Ring"),
        ("Bracelet", "Bracelet"),
        ("Elf Ear Cuffs", "Elf Ear Cuffs"),
        ("Wedding Rings", "Wedding Rings"),
        ("Anklets", "Anklets"),
        ("Brooch", "Brooch"),
        ("Solitaire Ring", "Solitaire Ring"),
        ("Toe Ring", "Toe Ring"),
        ("Medallion", "Medallion"),
        ("Hairpin", "Hairpin"),
    )
    category = models.CharField(max_length=50, choices=type)
    description = models.TextField()
    price = models.FloatField()
    images = models.ImageField(upload_to="photos")


class Cart(models.Model):
    userid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    productid = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    qty = models.PositiveIntegerField(default=0)


class Orders(models.Model):
    orderid = models.IntegerField(primary_key=True)
    userid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    productid = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    qty = models.PositiveIntegerField(default=0)


class Address(models.Model):
    userid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    contactnum = models.IntegerField()
    addr = models.TextField()
    pincode = models.IntegerField()


class Payment(models.Model):
    receiptid = models.IntegerField(primary_key=True)
    orderid = models.ForeignKey(Orders, on_delete=models.SET_NULL, null=True)
    userid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    productid = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    totalprice = models.FloatField()
