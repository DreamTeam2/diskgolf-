from django.contrib import admin

from models import Tim
from hracTimu.admin import HracTimuAdmin
from hrac.admin import HracAdmin
from zapas.admin import ZapasAdmin2

class TimAdminSelf(admin.ModelAdmin):
    list_display = ['nazov','kategoria_turnaju', 'klub']
    list_filter = ['kategoria_turnaju', 'klub']
    search_fields = ['nazov']
    inlines = [HracTimuAdmin, ZapasAdmin2]

admin.site.register(Tim, TimAdminSelf)


class TimAdmin(admin.StackedInline):
    model = Tim
