"""
WSGI config for nphiretest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nphiretest.settings")

application = get_wsgi_application()


def startup_code():
    from  threading import Thread
    from .smssender import AsyncManager
    from . import shared_object
    shared_object.manager = AsyncManager()
    proc = Thread(target=shared_object.manager.do_stuff)
    proc.start()

startup_code()  # we need to execute this code only one time, when application starts. 