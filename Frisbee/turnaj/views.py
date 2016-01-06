#-*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404,render_to_response,RequestContext
from .models import Turnaj
from zapas.models import Zapas
from tim.models import Tim
from kategoriaTurnaju.models import KategoriaTurnaju
import django_tables2 as tables
from django_tables2 import RequestConfig
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.utils.encoding import smart_unicode


class BaseSimpleTable(tables.Table):
    kategoria = tables.Column(verbose_name= 'Kategória',orderable=True)
    datum_od = tables.Column(verbose_name= 'Dátum od',orderable=True)
    datum_do = tables.Column(verbose_name= 'Dátum do',orderable=True)
    datum_zapisu = tables.Column(verbose_name= 'Dátum zápisu',orderable=True)
    report = tables.Column(verbose_name= 'Report',orderable=True)
    
    class Meta:
        model = Turnaj
        fields = ('kategoria','datum_od','datum_do','datum_zapisu','report')
        attrs = {"class": "paleblue"}
        orderable = True
        
    def render_kategoria(self,record):
        vysledok = ''
        pocet = 0
        for kategoria in record.kategoria:
            vysledok += smart_unicode(kategoria)
            pocet+=1
            if pocet != len(record.kategoria):
                vysledok+=', '
        if vysledok=='':
            return '—'
        return vysledok
    
    def render_zapasy(self,record):
        return mark_safe('<a href="'+reverse("zobraz_zapasy_turnaja", args=[record.id])+'">Zobraz</a>')

class SimpleTableKlikolNaStat(BaseSimpleTable):
    kategoria = tables.Column(verbose_name= 'Kategória',orderable=True)
    datum_od = tables.Column(verbose_name= 'Dátum od',orderable=True)
    datum_do = tables.Column(verbose_name= 'Dátum do',orderable=True)
    datum_zapisu = tables.Column(verbose_name= 'Dátum zápisu',orderable=True)
    report = tables.Column(verbose_name= 'Report',orderable=True)
    nazov = tables.LinkColumn('zobraz_timi_turnaja', args=[tables.A('id')], orderable=True, empty_values=(), verbose_name= 'Názov')
    mesto = tables.LinkColumn('zobraz_turnaje_mesta',args=[tables.A('mesto')],verbose_name= 'Mesto',orderable=True)
    zapasy = tables.LinkColumn('zobraz_zapasy_turnaja',args=[tables.A('id')], orderable=False, empty_values=(), verbose_name= 'Zápasy')
    
    class Meta:
        model = Turnaj
        fields = ('nazov','kategoria','datum_od','datum_do','mesto','datum_zapisu','report')
        attrs = {"class": "paleblue"}
        orderable = True

class SimpleTableKlikolNaMesto(BaseSimpleTable):
    kategoria = tables.Column(verbose_name= 'Kategória',orderable=True)
    datum_od = tables.Column(verbose_name= 'Dátum od',orderable=True)
    datum_do = tables.Column(verbose_name= 'Dátum do',orderable=True)
    datum_zapisu = tables.Column(verbose_name= 'Dátum zápisu',orderable=True)
    report = tables.Column(verbose_name= 'Report',orderable=True)
    nazov = tables.LinkColumn('zobraz_timi_turnaja', args=[tables.A('id')], orderable=True, empty_values=(), verbose_name= 'Názov')
    stat = tables.LinkColumn('zobraz_turnaje_statu',args=[tables.A('stat')],verbose_name= 'Štát',orderable=True)
    zapasy = tables.LinkColumn('zobraz_zapasy_turnaja',args=[tables.A('id')], orderable=False, empty_values=(), verbose_name= 'Zápasy')
    
    class Meta:
        model = Turnaj
        fields = ('nazov','kategoria','datum_od','datum_do','stat','datum_zapisu','report')
        attrs = {"class": "paleblue"}
        orderable = True
        
class SimpleTable(BaseSimpleTable):
    kategoria = tables.Column(verbose_name= 'Kategória',orderable=True)
    datum_od = tables.Column(verbose_name= 'Dátum od',orderable=True)
    datum_do = tables.Column(verbose_name= 'Dátum do',orderable=True)
    datum_zapisu = tables.Column(verbose_name= 'Dátum zápisu',orderable=True)
    report = tables.Column(verbose_name= 'Report',orderable=True)
    nazov = tables.LinkColumn('zobraz_timi_turnaja', args=[tables.A('id')], orderable=True, empty_values=(), verbose_name= 'Názov')
    stat = tables.LinkColumn('zobraz_turnaje_statu',args=[tables.A('stat')],verbose_name= 'Štát',orderable=True)
    mesto = tables.LinkColumn('zobraz_turnaje_mesta',args=[tables.A('mesto')],verbose_name= 'Mesto',orderable=True)
    zapasy = tables.LinkColumn('zobraz_zapasy_turnaja',args=[tables.A('id')], orderable=False, empty_values=(), verbose_name= 'Zápasy')
    
    class Meta:
        model = Turnaj
        fields = ('nazov','kategoria','datum_od','datum_do', 'stat','mesto','datum_zapisu','report')
        attrs = {"class": "paleblue"}
        orderable = True
    
        
        
def turnaj(request):
    nazov = smart_unicode("Turnaje")
    queryset = Turnaj.objects.all()
    for turnaj in queryset:
        kategorieturnaju = KategoriaTurnaju.objects.filter(turnaj=turnaj.id)
        turnaj.kategoria = kategorieturnaju
    table = SimpleTable(queryset)
    RequestConfig(request).configure(table)
    obsah = mark_safe("<h1>" + nazov + "</h1><section>" + smart_unicode("Zobrazenie všetkých Turnajov") + "</section>")
    return render_to_response("table.html", {"table": table,"nazov":nazov,"obsah":obsah},context_instance=RequestContext(request))

    
   # return render (request , "turnaj.html" , {'turnaje': turnaje })
# Create your views here.

from tim.views import SimpleTableKlikolTurnaj
from zapas.views import SimpleTableOdTurnaja 

def zobraz_zapasy_turnaja(request,id):
    nazov = smart_unicode("Zápasy Turnaja")
    kategorieTurnajov = KategoriaTurnaju.objects.filter(turnaj=id)
    queryset = Zapas.objects.filter(kategoria_turnaju__in=kategorieTurnajov)
    table = SimpleTableOdTurnaja(queryset)
    RequestConfig(request).configure(table)
    turnaj = Turnaj.objects.filter(id=id)
    try:
        obsah = mark_safe("<h1>" + nazov + " " + smart_unicode(turnaj[0]) + "</h1><section>" + smart_unicode("Zobrazenie zápasou  Turnaja") + "</section>")
    except IndexError:
        obsah = mark_safe("<h1>NEEXISTUJU ZÁPASY PRE DANÝ TURNAJ</h1>")
        table=Zapas.objects.none()
    return render_to_response("table.html", {"table": table,"nazov":nazov,"obsah":obsah},context_instance=RequestContext(request))

def zobraz_timi_turnaja(request,id_turnaja):
    nazov = smart_unicode("Tímy Turnaja")
    kategorieTurnajov = KategoriaTurnaju.objects.filter(turnaj=id_turnaja)
    queryset= Tim.objects.filter(id__in=kategorieTurnajov)
    table = SimpleTableKlikolTurnaj(queryset)
    RequestConfig(request).configure(table)
    
    turnaj = Turnaj.objects.filter(id=id_turnaja)
    try:
        obsah = mark_safe("<h1>" + nazov + " " + smart_unicode(turnaj[0]) + "</h1><section" + smart_unicode("Zobrazenie Tímov  Turnaja ") + "</section>")
    except IndexError:
        obsah = mark_safe("<h1>NEEXISTUJU TÍMY PRE DANÝ TURNAJ</h1>")
    return render_to_response("table.html", {"table": table,"nazov":nazov,"obsah":obsah},context_instance=RequestContext(request))

def zobraz_turnaje_statu(request,stat):
    nazov = smart_unicode("Turnaje Štátu")
    queryset= Turnaj.objects.filter(stat=stat)
    table = SimpleTableKlikolNaStat(queryset)
    obsah = mark_safe("<h1>" + nazov + " " + smart_unicode(queryset[0].stat) + "</h1><section>" + smart_unicode("Zobrazenie turnajov v danom štáte") + "</section>")
    RequestConfig(request).configure(table)
    return render_to_response("table.html", {"table": table,"nazov":nazov,"obsah":obsah},context_instance=RequestContext(request))  

def zobraz_turnaje_mesta(request,mesto):
    nazov = smart_unicode("Turnaje Mesta")
    queryset= Turnaj.objects.filter(mesto=mesto)
    table = SimpleTableKlikolNaMesto(queryset)
    RequestConfig(request).configure(table)
    obsah = mark_safe("<h1>" + nazov + " " + smart_unicode(queryset[0].mesto) + "</h1><section>" + smart_unicode("Zobrazenie turnajov v danom meste") + "</section>")
    return render_to_response("table.html", {"table": table,"nazov":nazov,"obsah":obsah},context_instance=RequestContext(request))  
    
        