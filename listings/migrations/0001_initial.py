# Generated by Django 3.2.7 on 2022-04-27 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing_id', models.IntegerField(verbose_name='Listing_id')),
                ('title', models.CharField(max_length=140, verbose_name='Title')),
                ('photo', models.ImageField(upload_to='', verbose_name='Photo')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('description', models.TextField(max_length=4000, verbose_name='Description')),
            ],
        ),
    ]
