# Generated by Django 5.1.2 on 2024-10-19 09:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactnum', models.IntegerField()),
                ('addr', models.TextField()),
                ('pincode', models.IntegerField()),
                ('userid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('orderid', models.IntegerField(primary_key=True, serialize=False)),
                ('qty', models.PositiveIntegerField(default=0)),
                ('userid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productid', models.IntegerField(primary_key=True, serialize=False)),
                ('productname', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Earrings', 'Earrings'), ('Cocktail Ring', 'Cocktail Ring'), ('Necklace', 'Necklace'), ('Bangle', 'Bangle'), ('Mangal Sutra', 'Mangal Sutra'), ('Chain', 'Chain'), ('Engagement Ring', 'Engagement Ring'), ('Bracelet', 'Bracelet'), ('Elf Ear Cuffs', 'Elf Ear Cuffs'), ('Wedding Rings', 'Wedding Rings'), ('Anklets', 'Anklets'), ('Brooch', 'Brooch'), ('Solitaire Ring', 'Solitaire Ring'), ('Toe Ring', 'Toe Ring'), ('Medallion', 'Medallion'), ('Hairpin', 'Hairpin')], max_length=50)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('images', models.ImageField(upload_to='photos')),
                ('userid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('receiptid', models.IntegerField(primary_key=True, serialize=False)),
                ('totalprice', models.FloatField()),
                ('orderid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.orders')),
                ('userid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('productid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
        migrations.AddField(
            model_name='orders',
            name='productid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.product'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField(default=0)),
                ('userid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('productid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
    ]
