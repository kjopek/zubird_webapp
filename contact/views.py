# -*- coding: utf-8 -*-

from forms import ContactForm
from django.shortcuts import render_to_response
from django.template import Context
from django.views.decorators.cache import cache_page
from django.utils.log import getLogger
from django.core.context_processors import csrf

# Create your views here.
@cache_page(60*15)
def index(request):
    # TODO 
    logger = getLogger()
    form = ContactForm()
    logger.info('Form: '+str(form))
    d = {'form':form}
    d.update(csrf(request))
    return render_to_response('base.html', Context(d))

def send(request):
    # TODO
    return render_to_response('base.html', {})
