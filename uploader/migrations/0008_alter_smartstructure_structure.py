# Generated by Django 3.2.7 on 2022-07-01 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0007_smartarchive_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartstructure',
            name='structure',
            field=models.CharField(max_length=10000000000, verbose_name='Structure'),
        ),
    ]