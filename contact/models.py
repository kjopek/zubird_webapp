# -*- coding: utf-8 -*-

from django.contrib.gis.db import models
from django.utils.translation import ugettext as _

# Create your models here.

class Message(models.Model):
    JOB_TYPE = ((1, _(u'Repairs / building roads')), 
            (2, _(u'Sett')),
            (3, _(u'General repairs of building')))
    
    username = models.CharField(_(u'First and last name'), max_length=30)
    email = models.EmailField(_(u'Email'))
    phone = models.CharField(_(u'Phone'), max_length=12)
    location = models.CharField(_(u'Location'), max_length=50)
    job = models.IntegerField(_(u'Job type'), choices=JOB_TYPE)
    description = models.TextField(_(u'Job description'))
    area = models.PolygonField(_(u'Job area'))
    added = models.DateTimeField(_(u'Added'), auto_now_add=True)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.username

    class Meta(object):
        verbose_name_plural = _(u'Messages')
