# Generated by Django 3.2.5 on 2021-12-04 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_auto_20211204_0933'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookOfTheWeek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Книга недели',
            },
        ),
    ]
