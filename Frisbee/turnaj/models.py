from django.db import models
from datetime import date, timedelta
# Create your models here.
from django.utils.encoding import smart_unicode

class Turnaj(models.Model):
    nazov = models.CharField(max_length = 50)
    
    day = date.today().weekday()
    datum_od = None
    datum_do = None
    if day < 6: 
        datum_od = models.DateField(default=(date.today() - timedelta(days=day+2)))
        datum_do = models.DateField(default=(date.today() - timedelta(days=day+1)))
    else:
        datum_od = models.DateField(default=(date.today() - timedelta(days=1)))
        datum_do = models.DateField(default=(date.today()))
    mesto = models.CharField(max_length = 50, default = '')
    stat = models.CharField(max_length = 50, default = '')
    datum_zapisu = models.DateField(default=date.today)
    report = models.CharField(max_length = 150, default = '', null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Turnaje'
        
    def __str__(self):
        return self.nazov
    
    def __repr__(self):
        return self.nazov
    
    def __unicode__(self): 
        return smart_unicode(self.nazov)