import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')  # "config" loyihangiz nomi bo'lishi kerak

application = get_wsgi_application()
