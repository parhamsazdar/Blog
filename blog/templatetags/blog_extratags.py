from datetime import datetime

from django import template
from khayyam import JalaliDatetime
from persiantools import jdatetime
from django import template

register = template.Library()

@register.filter
def jalali_date(value):
    date = JalaliDatetime(value).strftime("%A %d %B %Y ساعت %I:%M %p" )
    return date
