# Generated by Django 4.2.6 on 2023-10-19 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy_app', '0002_alter_cart_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]