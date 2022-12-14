# Generated by Django 3.2.7 on 2022-05-01 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=30, verbose_name='Login')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('shop_name', models.CharField(max_length=20, verbose_name='Shop')),
                ('shop_connection', models.BinaryField(default=False, verbose_name='Shop Connetion')),
                ('subscribtion', models.BinaryField(default=False, verbose_name='Subscribtion')),
            ],
        ),
    ]
