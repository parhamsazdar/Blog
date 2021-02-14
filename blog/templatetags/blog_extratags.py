from khayyam import JalaliDatetime

from django import template

register = template.Library()


@register.filter
def jalali_date(value):
    date = JalaliDatetime(value).strftime("%A %d %B %Y ساعت %I:%M %p")
    return date


@register.filter
def jalali_date_no_hour(value):
    date = JalaliDatetime(value).strftime("%A %d %B %Y")
    return date


@register.filter
def string_charp(value):
    return "#" + "category" + str(value)


@register.filter
def string(value):
    return "category" + str(value)


