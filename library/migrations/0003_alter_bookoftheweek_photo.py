# Generated by Django 3.2.9 on 2021-11-29 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20211129_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookoftheweek',
            name='photo',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
