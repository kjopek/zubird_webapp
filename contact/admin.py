from django.contrib.gis import admin
from contact.models import Message

class MessageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Message, MessageAdmin)