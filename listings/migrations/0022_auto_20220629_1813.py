# Generated by Django 3.2.7 on 2022-06-29 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0021_auto_20220629_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='competitor',
            name='is_sold_lisitngs',
            field=models.BooleanField(blank=True, default=None, verbose_name='Is open sold listing?'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='CompetitorTopSales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(editable=False)),
                ('sales', models.IntegerField(verbose_name='Number of Sales on date')),
                ('competitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.competitor')),
            ],
        ),
        migrations.CreateModel(
            name='CompetitorSalesOnDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(editable=False)),
                ('sales', models.IntegerField(verbose_name='Number of Sales on date')),
                ('competitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.competitor')),
            ],
        ),
    ]
