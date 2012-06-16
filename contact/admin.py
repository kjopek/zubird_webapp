from django.contrib.gis import admin
from contact.models import Message

class MessageAdmin(admin.GeoModelAdmin):
    pass

admin.site.register(Message, MessageAdmin)