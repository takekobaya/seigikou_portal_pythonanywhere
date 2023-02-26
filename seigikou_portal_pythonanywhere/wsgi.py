"""
WSGI config for seigikou_portal_pythonanywhere project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
import dotenv

#.envから環境変数を読み込む
dotenv.load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seigikou_portal_pythonanywhere.settingsdevelopment')

application = get_wsgi_application()

#from whitenoise.django import DjangoWhiteNoise
#application = DjangoWhiteNoise(application)