# Generated by Django 2.2.7 on 2020-05-05 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0017_auto_20200505_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='expensepaidamount',
            name='balance',
            field=models.FloatField(default=0, null=True),
        ),
    ]