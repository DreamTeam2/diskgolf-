"""Frisbee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.contrib import admin

admin.autodiscover()

from django.conf.urls import include, url

admin.site.site_header = 'Frisbee Administracia'

urlpatterns = [
    #navigacia
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','Frisbee.views.index', name="index"),
    url(r'^index$','Frisbee.views.index', name="index"),
    url(r'^hraci$','hrac.views.hrac',name="hrac"),
    url(r'^klub$','klub.views.klub',name="klub"),
    url(r'^zapas$','zapas.views.zapas',name="zapas"),
    url(r'^turnaj$','turnaj.views.turnaj',name="turnaj"),
    url(r'^tim$','tim.views.tim',name="tim"),
    #kliknutia pri turnaji
    url(r'^turnaj_zapas=(?P<id>[0-9]+)$','turnaj.views.zobraz_zapasy_turnaja', name='zobraz_zapasy_turnaja'),
    url(r'^turnaj_stat=(?P<stat>.*)$','turnaj.views.zobraz_turnaje_statu', name='zobraz_turnaje_statu'),
    url(r'^turnaj_tim=(?P<id_turnaja>[0-9]+)$','turnaj.views.zobraz_timi_turnaja', name='zobraz_timi_turnaja'),
    url(r'^turnaj_mesto=(?P<mesto>.*)$','turnaj.views.zobraz_turnaje_mesta', name='zobraz_turnaje_mesta'),
    # kliknutie pri timoch
    url(r'^tim_hrac=(?P<id_timu>[0-9]+)$','tim.views.zobraz_hracov_timu', name='zobraz_hracov_timu'),
    url(r'^tim_klub=(?P<id_klubu>[0-9]+)$','tim.views.zobraz_hracov_klubu', name='zobraz_hracov_klubu'),
    url(r'^tim_zapas=(?P<id_timu>.*)$','tim.views.zobraz_zapasy_timu', name='zobraz_zapasy_timu'),
    # kliknutia pri hracovy
    url(r'^turnaj_hraca=(?P<id>[0-9]+)$','hrac.views.turnaj_hraca', name='turnaj_hraca'),
    url(r'^klub_hrac=(?P<id>[0-9]+)$','hrac.views.hraci_klubu', name='hraci_klubu'),

    

]
