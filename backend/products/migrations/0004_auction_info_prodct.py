# Generated by Django 3.2.8 on 2021-11-13 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_auction_info_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction_info',
            name='prodct',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.product_master'),
            preserve_default=False,
        ),
    ]
