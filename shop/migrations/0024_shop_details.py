# Generated by Django 2.2.5 on 2019-10-09 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_auto_20191003_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_charge', models.PositiveIntegerField(default=None)),
            ],
        ),
    ]