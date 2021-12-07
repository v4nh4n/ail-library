# Generated by Django 3.2.5 on 2021-12-03 14:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20211129_1549'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ailbook',
            options={'verbose_name_plural': 'Книги AIL'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterModelOptions(
            name='bookoftheweek',
            options={'verbose_name_plural': 'Книга недели'},
        ),
        migrations.AlterModelOptions(
            name='recommended',
            options={'verbose_name_plural': 'Рекомендованые'},
        ),
        migrations.AlterModelOptions(
            name='winner',
            options={'verbose_name_plural': 'Победитель'},
        ),
        migrations.AddField(
            model_name='ailbook',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ailbook',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 12, 3, 14, 5, 33, 476061, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]