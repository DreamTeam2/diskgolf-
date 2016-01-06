from django.db import models
from datetime import date
# Create your models here.
from django.utils.encoding import smart_unicode

class Turnaj(models.Model):
    nazov = models.CharField(max_length = 50)
    datum_od = models.DateField(default=date.today)
    datum_do = models.DateField(default=date.today)
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