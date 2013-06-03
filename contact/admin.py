from django.contrib.gis import admin
from models import Message

#GMAP = GoogleMap(key='abcdefg')

class MessageAdmin(admin.OSMGeoAdmin):
    pass

#class GoogleAdmin(admin.OSMGeoAdmin):
#    extra_js = [GMAP.api_url + GMAP.key]
#    map_template = 'gis/admin/google.html'

admin.site.register(Message, MessageAdmin)
