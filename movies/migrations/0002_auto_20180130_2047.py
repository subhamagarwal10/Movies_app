# Generated by Django 2.0 on 2018-01-30 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='Rating',
            field=models.IntegerField(),
        ),
    ]
