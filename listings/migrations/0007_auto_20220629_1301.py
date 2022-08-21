# Generated by Django 3.2.7 on 2022-06-29 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_ver_account_verified'),
        ('listings', '0006_auto_20220629_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='account',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, to='main.account'),
        ),
        migrations.AddField(
            model_name='listing',
            name='shop',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, to='listings.shop'),
        ),
    ]
