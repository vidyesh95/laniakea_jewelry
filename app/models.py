from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class CustomManager(models.Manager):
    def earrings_list(self):
        return self.filter(category__exact="Earrings")

    def cocktail_ring_list(self):
        return self.filter(category__exact="Cocktail Ring")

    def necklace_list(self):
        return self.filter(category__exact="Necklace")

    def bangle_list(self):
        return self.filter(category__exact="Bangle")

    def mangal_sutra_list(self):
        return self.filter(category__exact="Mangal Sutra")

    def chain_list(self):
        return self.filter(category__exact="Chain")

    def engagement_ring_list(self):
        return self.filter(category__exact="Engagement Ring")

    def bracelet_list(self):
        return self.filter(category__exact="Bracelet")

    def elf_ear_cuffs_list(self):
        return self.filter(category__exact="Elf Ear Cuffs")

    def wedding_rings_list(self):
        return self.filter(category__exact="Wedding Rings")

    def anklets_list(self):
        return self.filter(category__exact="Anklets")

    def brooch_list(self):
        return self.filter(category__exact="Brooch")

    def solitaire_ring_list(self):
        return self.filter(category__exact="Solitaire Ring")

    def toe_ring_list(self):
        return self.filter(category__exact="Toe Ring")

    def medallion_list(self):
        return self.filter(category__exact="Medallion")

    def hairpin_list(self):
        return self.filter(category__exact="Hairpin")


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
    objects = models.Manager()
    productmanager = CustomManager()


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
