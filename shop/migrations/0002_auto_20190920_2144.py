# Generated by Django 2.2.5 on 2019-09-20 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.PositiveIntegerField(default=None)),
                ('address', models.TextField(blank=True)),
                ('phone', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ('customer_id',),
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.PositiveIntegerField(default=None)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
            ],
            options={
                'ordering': ('product_id',),
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('off_percent', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('product_id', models.PositiveIntegerField(default=None)),
                ('category_id', models.PositiveIntegerField(default=None)),
                ('order_size', models.PositiveIntegerField(default=None)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
