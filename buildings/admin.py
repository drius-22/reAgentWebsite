from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(country)
admin.site.register(province)
admin.site.register(city)
admin.site.register(location)
admin.site.register(property)
admin.site.register(property_images)
