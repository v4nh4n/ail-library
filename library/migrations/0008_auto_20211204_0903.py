# Generated by Django 3.2.5 on 2021-12-04 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_auto_20211203_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ailbook',
            name='photo',
            field=models.CharField(max_length=9000),
        ),
        migrations.AlterField(
            model_name='book',
            name='photo',
            field=models.CharField(max_length=9000),
        ),
        migrations.AlterField(
            model_name='recommended',
            name='photo',
            field=models.CharField(max_length=9000),
        ),
    ]