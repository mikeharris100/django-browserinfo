import os
from django.conf import settings
from django import template
import browserinfo

register = template.Library()

BROWSERINFO_SCRIPT = None

def include_browserinfo():
    global BROWSERINFO_SCRIPT
    if BROWSERINFO_SCRIPT is None:
        if settings.DEBUG:
            BROWSERINFO_SCRIPT =  '<script type="text/javascript">%s</script>' % open(os.path.join(os.path.dirname(browserinfo.__file__), 'media', 'browserinfo', 'js', 'jquery-browser-info.js')).read()
        else:
            BROWSERINFO_SCRIPT = '<script type="text/javascript" src="%s%s"></script>' % (settings.MEDIA_URL, 'js/jquery-browser-info.js')

    return BROWSERINFO_SCRIPT



register.simple_tag(include_browserinfo)


