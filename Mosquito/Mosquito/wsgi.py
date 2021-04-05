"""
WSGI config for Mosquito project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


application = get_wsgi_application()
from Mosquito.settings import DEBUG
if not DEBUG:
    from dj_static import Cling
    application = Cling(get_wsgi_application())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Mosquito.settings')

application = get_wsgi_application()
