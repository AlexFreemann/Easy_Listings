# Generated by Django 3.2.7 on 2022-06-29 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0014_remove_shop_account'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Shop',
        ),
    ]