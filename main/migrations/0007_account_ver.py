# Generated by Django 3.2.7 on 2022-05-10 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_account_shop_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='ver',
            field=models.BooleanField(default=False, verbose_name='Verification'),
        ),
    ]
