# Generated by Django 2.2.7 on 2020-04-24 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addroommate',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
