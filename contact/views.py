# -*- coding: utf-8 -*-

import forms
from django.shortcuts import render_to_response
# Create your views here.

def index(request):
    # TODO 
    d = {}
    return render_to_response('base.html', Context(d))

def send(request):
    # TODO
    return ''
