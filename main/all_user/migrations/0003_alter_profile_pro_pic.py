# Generated by Django 4.2.6 on 2023-10-17 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_user', '0002_alter_profile_pro_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pro_pic',
            field=models.ImageField(blank=True, default='pro.png', null=True, upload_to='pro_pic/'),
        ),
    ]
