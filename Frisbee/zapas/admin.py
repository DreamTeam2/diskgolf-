from django.contrib import admin

from models import Zapas


class ZapasAdminSelf(admin.ModelAdmin):
    list_display = ['kategoria_turnaju', 'tim_1', 'tim_2', 'vysledok_1', 'vysledok_2']
    list_filter = ['kategoria_turnaju']
    search_fields = ['tim_1', 'tim_2']

admin.site.register(Zapas, ZapasAdminSelf)    
    
class ZapasAdmin(admin.StackedInline):
    model = Zapas
    
class ZapasAdmin2(admin.StackedInline):
    model = Zapas
    fk_name = 'tim_1'