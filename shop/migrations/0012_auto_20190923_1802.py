# Generated by Django 2.2.5 on 2019-09-23 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20190923_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='dob',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
