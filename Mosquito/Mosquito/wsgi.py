import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling
from Mosquito.settings import DEBUG
application = get_wsgi_application()
if not DEBUG:
    from dj_static import Cling
    application = Cling(get_wsgi_application())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Mosquito.settings')

application = get_wsgi_application()
