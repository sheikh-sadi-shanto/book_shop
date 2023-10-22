# Generated by Django 4.2.6 on 2023-10-15 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('e_book', '0003_alter_book_details_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_details',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_name', to='e_book.book_chapter'),
        ),
    ]
