from django.db import models
from django.contrib.auth.models import User

class BrowserInfo(models.Model):
    user = models.ForeignKey(User)
    # country
    # region
    # city
    # isp
    ip = models.IPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=255, null=True, blank=True)
    # os
    # platform
    # browser
    timezone = models.CharField(max_length=3, null=True, blank=True)
    # css_support
    colour_depth = models.CharField(max_length=50, null=True, blank=True)
    # js_support
    # js_enabled
    screen_height = models.PositiveIntegerField()
    screen_width = models.PositiveIntegerField()
    browser_height = models.PositiveIntegerField()
    browser_width = models.PositiveIntegerField()
    # images_enabled
    # png_support
