# Generated by Django 4.2.6 on 2023-11-05 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy_app', '0003_order_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingAdress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('number', models.IntegerField()),
                ('distric', models.CharField(max_length=120)),
                ('address', models.TextField()),
            ],
        ),
    ]
