# Generated by Django 3.1 on 2020-08-15 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokeApi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evolution',
            name='level',
            field=models.IntegerField(default=0),
        ),
    ]
