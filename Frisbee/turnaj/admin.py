from django.contrib import admin

from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin
from turnaj.models import Turnaj
from tim.models import Tim
from kategoriaTurnaju.models import KategoriaTurnaju
from hracTimu.models import HracTimu
from kategoriaTurnaju.admin import KategoriaTurnajuAdmin
from zapas.models import Zapas


class HracInlineAdmin(SuperInlineModelAdmin, admin.TabularInline):
    model = HracTimu

class TimInlineAdmin(SuperInlineModelAdmin, admin.StackedInline):
    model = Tim
    inlines = (HracInlineAdmin,)

class ZapasInlineAdmin(SuperInlineModelAdmin, admin.TabularInline):
    model = Zapas
    
class KategoriaTurnajuInlineAdmin(SuperInlineModelAdmin, admin.StackedInline):
    model = KategoriaTurnaju
    inlines = (TimInlineAdmin,ZapasInlineAdmin, )

class TurnajAdmin(SuperModelAdmin):
    list_display = ['nazov','datum_od', 'datum_do', 'mesto', 'stat', 'datum_zapisu', 'report']
    list_filter = ['mesto', 'stat']
    search_fields = ['nazov']
    inlines = [KategoriaTurnajuInlineAdmin,]

admin.site.register(Turnaj, TurnajAdmin)