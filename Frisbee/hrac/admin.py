from django.contrib import admin

from models import Hrac
from django.contrib.auth.models import User
from hracTimu.admin import HracTimuAdmin

class HracAdminSelf(admin.ModelAdmin):
    list_display = ['prezivka','krstne_meno', 'priezvisko', 'pohlavie', 'telefonne_cislo', 'miesto_bydliska', 'datum_narodenia', 'uzivatel', 'klub', 'foto', 'poznamka']
    list_filter = ['klub']
    search_fields = ['prezivka', 'krstne_meno', 'priezvisko']
    inlines = [HracTimuAdmin]

admin.site.register(Hrac, HracAdminSelf)


class HracAdmin(admin.StackedInline):
    model = Hrac
    
class UserAdmin(admin.ModelAdmin):
    inlines = [HracAdmin]
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)