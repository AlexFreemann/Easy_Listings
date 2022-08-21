# Generated by Django 3.2.7 on 2022-06-29 13:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_ver_account_verified'),
        ('listings', '0008_auto_20220629_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='account',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, to='main.account'),
            preserve_default=False,
        ),
    ]