#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import Http404

class CertSecurityMiddleware(object):
    
    def process_request(self, request):
        if hasattr(request, 'path'):
            if request.path.startswith('/admin'):
                if ((not request.META.has_key('SSL_CLIENT_VERIFIED')) or
                        request.META['SSL_CLIENT_VERIFIED'] != 'SUCCESS'):
                    raise Http404
