# Generated by Django 3.2.7 on 2022-06-30 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_ver_account_verified'),
        ('uploader', '0002_variation_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images/static', verbose_name='Static Photo')),
                ('name', models.CharField(max_length=25, verbose_name='Name for App your photo')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.account')),
            ],
        ),
    ]
