from django.contrib import admin

from models import HracTimu

class HracTimuAdminSelf(admin.ModelAdmin):
    list_display = ['hrac','tim']
    search_fields = ['hrac', 'tim']
    

admin.site.register(HracTimu, HracTimuAdminSelf)


class HracTimuAdmin(admin.StackedInline):
    model = HracTimu