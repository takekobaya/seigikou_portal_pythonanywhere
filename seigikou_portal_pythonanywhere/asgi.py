"""
ASGI config for seigikou_portal_pythonanywhere project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
import dotenv

#.envから環境変数を読み込む
dotenv.load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seigikou_portal_pythonanywhere.settings.production')

application = get_asgi_application()
