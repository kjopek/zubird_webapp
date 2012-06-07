# -*- coding: utf-8 -*-

import floppyforms as forms
#import django.forms as forms
from models import Message
class GMapPolygonWidget(forms.gis.BaseGMapWidget,
                        forms.gis.PolygonWidget):
    pass

class ContactForm(forms.Form):
    username = forms.CharField(label=_(u'First and last name'), max_length=30)
    email = forms.EmailField(label=_(u'Email'))
    phone = forms.RegexField('\d{9}', label=_(u'Phone'), max_length=12)
    location = forms.CharField(label=_(u'Location'), max_length=50)
    job = forms.ChoiceField(label=_(u'Job type'), choices=Message.JOB_TYPE)
    description = forms.TextField(label=_(u'Job description'))
    area = forms.gis.PolygonField(label=_(u'Area'), widget=GMapPolygonWidget)
    