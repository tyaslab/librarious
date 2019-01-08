from django.contrib import admin
from django.contrib.gis import admin as gis_admin

from .models import *


admin.site.register(Member)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Review)

gis_admin.site.register(WorldBorder, gis_admin.GeoModelAdmin)
