# Generated by Django 4.0.4 on 2022-07-14 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0015_filelistinguploader'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filelistinguploader',
            name='file',
            field=models.FileField(upload_to='listing_files/listings', verbose_name='File'),
        ),
    ]
