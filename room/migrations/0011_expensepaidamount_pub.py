# Generated by Django 2.2.7 on 2020-05-01 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0010_pubbillamount_total_amt'),
    ]

    operations = [
        migrations.AddField(
            model_name='expensepaidamount',
            name='pub',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='room.PUBBillAmount'),
        ),
    ]
