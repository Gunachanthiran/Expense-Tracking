from django.db import models

# Create your models here.
class AddRoommate(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    date = models.DateField(auto_now=True)

    class Meta:
        db_table = "AddRoommate"

class AddExpenses(models.Model):
    name = models.ForeignKey(AddRoommate, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    item_price = models.FloatField()
    date = models.DateField()

    class Meta:
        db_table = "AddExpenses"

class PUBBillAmount(models.Model):
    pre_date = models.DateField(null=True)
    prev_read = models.FloatField(default=0)
    cur_date = models.DateField(null=True)
    cur_read = models.FloatField(default=0)
    total_units = models.FloatField(default=0)
    refuse_amt = models.FloatField(default=0)
    water_amt = models.FloatField(default=0)
    gst = models.FloatField(default=0)
    total_amt = models.FloatField(null=True, default=0)
    food_date = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = "PUBBillAmount"

class ExpensePaidAmount(models.Model):
    month_year = models.CharField(max_length=50)
    name = models.ForeignKey(AddRoommate, on_delete=models.CASCADE)
    no_of_days = models.IntegerField(null=True)
    food_expense = models.FloatField()
    total_paid_pub = models.FloatField(null=True, default=0)
    pub = models.FloatField(null=True, default=0)
    balance = models.FloatField(null=True, default=0)
    purchase = models.FloatField(null=True, default=0)

    class Meta:
        db_table = "ExpensePaidAmount"

    # mkvirtualenv --python=/usr/bin/python3.7  monito-virtualenv
    # source .virtualenvs/monito-virtualenv/bin/activate

    # python manage.py migrate --run-syncdb

    # class PUBBillAmount(models.Model):
    # date = models.DateField()
    # total_units = models.FloatField()
    # refuse_amt = models.FloatField()
    # water_amt = models.FloatField()
    # gst = models.FloatField()
    # total_amt = models.FloatField(null=True)
    # food_date = models.CharField(max_length=50, null=True)
