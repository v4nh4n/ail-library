# Generated by Django 3.2.5 on 2021-12-04 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_auto_20211204_0903'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BookOfTheWeek',
        ),
        migrations.AddField(
            model_name='ailbook',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
