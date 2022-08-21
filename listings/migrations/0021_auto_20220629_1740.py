# Generated by Django 3.2.7 on 2022-06-29 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_ver_account_verified'),
        ('listings', '0020_remove_shop_shop_connection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='shop',
        ),
        migrations.AddField(
            model_name='listing',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.account'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Shop',
        ),
    ]