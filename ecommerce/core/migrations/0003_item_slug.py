# Generated by Django 3.0.3 on 2020-03-11 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200310_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='test_product'),
            preserve_default=False,
        ),
    ]
