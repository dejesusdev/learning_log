from django.contrib import admin

from .models import Topic, Entry
# . In front of models tells Django to find it in the same directory

admin.site.register(Topic)
admin.site.register(Entry)