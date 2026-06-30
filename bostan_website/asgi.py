"""
ASGI config for bostan_website project.
"""
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bostan_website.settings')
application = get_asgi_application()
