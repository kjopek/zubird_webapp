# -*- coding: utf-8 -*-

from forms import ContactForm
from django.shortcuts import render_to_response
from django.template import Context
from django.views.decorators.cache import cache_page
from django.utils.log import getLogger

from django.core.context_processors import csrf
from django.core.mail import send_mail

from models import Message

logger = getLogger(__name__)

def main_page(request):
    form = ContactForm()
    d = {'form':form}
    d.update(csrf(request))
    return render_to_response('base.html', Context(d))

# Create your views here.
@cache_page(60*2)
def index(request):
    return main_page(request)

def send(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            
            msg = Message()
            msg.username = form.cleaned_data['username']
            msg.email = form.cleaned_data['email']
            msg.phone = form.cleaned_data['phone']
            msg.location = form.cleaned_data['location']
            msg.job = form.cleaned_data['job']
            msg.description = form.cleaned_data['description']
            msg.area = form.cleaned_data['area']
            
            try:
                msg.save()
            except Exception as e:
                import traceback
                logger.error(str(e))
                logger.error(traceback.format_exc())
                return render_to_response('error.html', {})
            
            return render_to_response('thanks.html', {})
        else:
            return render_to_response('base.html', Context({'form':form}))
    else:
        return main_page(request)
