# Generated by Django 3.2.7 on 2022-06-29 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_ver_account_verified'),
        ('listings', '0012_shop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.account'),
        ),
    ]
