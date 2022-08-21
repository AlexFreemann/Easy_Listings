# Generated by Django 4.0.4 on 2022-07-17 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_ver_account_verified'),
        ('uploader', '0016_alter_filelistinguploader_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticphoto',
            name='photo',
            field=models.ImageField(blank=True, default=True, upload_to='images/static/static_photos', verbose_name='Photo'),
        ),
        migrations.CreateModel(
            name='DynamicPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(blank=True, max_length=500, verbose_name='Path in smart archive')),
                ('name', models.CharField(max_length=25, verbose_name='Name for App your photo')),
                ('photo', models.ImageField(blank=True, default=True, upload_to='images/static/dynamic_photos', verbose_name='Photo')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.account')),
                ('archive', models.ForeignKey(blank=True, max_length=25, on_delete=django.db.models.deletion.CASCADE, to='uploader.smartarchive', verbose_name='Name of Archive, Manually uploaded is empty')),
            ],
        ),
    ]