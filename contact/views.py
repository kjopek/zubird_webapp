# -*- coding: utf-8 -*-

from forms import ContactForm
from django.shortcuts import render_to_response
from django.views.decorators.cache import cache_page

# Create your views here.
@cache_page(60*15)
def index(request):
    # TODO 
    form = ContactForm()
    d = {'form':form}
    return render_to_response('base.html', Context(d))

def send(request):
    # TODO
    return render_to_response('base.html', {})
