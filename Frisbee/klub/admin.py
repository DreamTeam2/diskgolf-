from django.contrib import admin

from models import Klub
from hrac.admin import HracAdmin

class KlubAdmin(admin.ModelAdmin):
    list_display = ['nazov']
    search_fields = ['nazov']
    inlines = [HracAdmin]

admin.site.register(Klub, KlubAdmin)