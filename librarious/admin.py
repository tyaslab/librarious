from django.contrib import admin
from .models import *


admin.site.register(Member)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Review)
