# Generated by Django 3.1.5 on 2021-01-29 19:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('licence_plate', models.CharField(max_length=20, verbose_name='License plate')),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
        migrations.CreateModel(
            name='CarType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True, verbose_name='Car Type')),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30, unique=True)),
                ('expiration_date', models.DateTimeField(blank=True, null=True, verbose_name='Coupon Expiration Date')),
                ('discount', models.IntegerField(help_text='%', verbose_name='Discount')),
                ('quantity', models.IntegerField(default=1, verbose_name='Quantity')),
                ('car_plate', models.CharField(max_length=20, verbose_name="Car's license plate")),
            ],
            options={
                'verbose_name': 'Coupon',
                'verbose_name_plural': 'Coupons',
            },
        ),
        migrations.CreateModel(
            name='WashType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True, verbose_name='Car Type')),
                ('percentage', models.IntegerField(default=100, verbose_name='Percentage of base price')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Note')),
                ('price', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Price')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('start_date', models.DateTimeField(verbose_name='Scheduled time')),
                ('end_date', models.DateTimeField(verbose_name='Scheduled time')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='wash.car')),
                ('coupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='wash.coupon')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to=settings.AUTH_USER_MODEL)),
                ('wash_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='wash.washtype')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.AddField(
            model_name='car',
            name='car_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cars', to='wash.cartype'),
        ),
    ]
