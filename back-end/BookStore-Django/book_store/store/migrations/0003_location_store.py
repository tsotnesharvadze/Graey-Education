# Generated by Django 3.1.5 on 2021-01-22 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210122_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('street_address', models.CharField(max_length=255)),
                ('zip', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='store', to='store.location')),
            ],
        ),
    ]
