# Generated by Django 3.2.7 on 2022-06-29 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0017_listing_shop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.shop'),
        ),
    ]
