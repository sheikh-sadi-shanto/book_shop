# Generated by Django 4.2.6 on 2023-10-10 06:01

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField(blank=True, default=0.0, null=True)),
                ('book_img', models.ImageField(default='default.jpg', upload_to='book_img')),
                ('user_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Book_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('page', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='page_name', to='e_book.ebook')),
            ],
        ),
        migrations.CreateModel(
            name='Book_chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_name', models.CharField(max_length=300)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_chapter', to='e_book.ebook')),
            ],
        ),
    ]
