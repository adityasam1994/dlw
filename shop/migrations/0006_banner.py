# Generated by Django 2.2.5 on 2019-09-20 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_product_sold'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, upload_to='banners/%Y/%m/%d')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
