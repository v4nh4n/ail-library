# Generated by Django 3.2.5 on 2021-12-04 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_bookoftheweek'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookOfTheWeek',
            new_name='RandomBook',
        ),
    ]
