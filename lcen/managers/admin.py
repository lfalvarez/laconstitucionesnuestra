from django.contrib import admin

from django.contrib import admin
from .models import Pais, Region, Distrito, Comuna



admin.site.register(Pais)
admin.site.register(Region)
admin.site.register(Distrito)
admin.site.register(Comuna)