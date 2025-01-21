# Register your models here.
from django.contrib import admin
from .models import Character, Characteristic, BuildRequest

admin.site.register(Character)
admin.site.register(Characteristic)
admin.site.register(BuildRequest)
