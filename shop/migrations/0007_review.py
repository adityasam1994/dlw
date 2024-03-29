# Generated by Django 2.2.5 on 2019-09-23 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.PositiveIntegerField(default=None)),
                ('review', models.TextField(default=None)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('rating', models.PositiveIntegerField(default=None)),
            ],
            options={
                'ordering': ('date',),
            },
        ),
    ]
