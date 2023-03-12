
# settings/__init__.py

from .production import *

try:
    from .development import *
except:
    pass