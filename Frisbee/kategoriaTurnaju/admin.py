from django.contrib import admin
from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin

from .models import KategoriaTurnaju
from hracTimu.models import HracTimu
from tim.models import Tim
from zapas.models import Zapas

class HracInlineAdmin(SuperInlineModelAdmin, admin.TabularInline):
    model = HracTimu

class TimInlineAdmin(SuperInlineModelAdmin, admin.StackedInline):
    model = Tim
    inlines = (HracInlineAdmin,)
    
class ZapasInlineAdmin(SuperInlineModelAdmin, admin.TabularInline):
    model = Zapas

class KategoriaTurnajuAdminSelf(SuperModelAdmin):
    list_display = ['turnaj', 'kategoria', 'pocet_timov']
    search_fields = ['turnaj', 'kategoria']
    inlines = (TimInlineAdmin,ZapasInlineAdmin,)

admin.site.register(KategoriaTurnaju, KategoriaTurnajuAdminSelf)

class KategoriaTurnajuAdmin(admin.StackedInline):
    model = KategoriaTurnaju