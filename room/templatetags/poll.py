from django import template
from datetime import datetime, date

register = template.Library()

def month_year_filt(value):
    if type(value) == str:
        convert_date = datetime.strptime(value, '%m, %Y')
        return convert_date
    if value is not None:
        return value.strftime('%B, %Y')

register.filter('month_year_filt', month_year_filt)