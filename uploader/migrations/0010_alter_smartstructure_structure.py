# Generated by Django 3.2.7 on 2022-07-01 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0009_alter_smartstructure_structure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartstructure',
            name='structure',
            field=models.CharField(max_length=10000000000, verbose_name='Structure'),
        ),
    ]
