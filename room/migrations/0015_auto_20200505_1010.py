# Generated by Django 2.2.7 on 2020-05-05 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0014_auto_20200505_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensepaidamount',
            name='pub',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='expensepaidamount',
            name='total_paid_pub',
            field=models.FloatField(default=0, null=True),
        ),
    ]
