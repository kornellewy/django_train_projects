# Generated by Django 3.0.3 on 2020-03-12 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_item_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_date',
            new_name='ordered_date',
        ),
    ]
