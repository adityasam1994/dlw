# Generated by Django 2.2.5 on 2019-09-30 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_address_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'ordering': ('name',)},
        ),
    ]
