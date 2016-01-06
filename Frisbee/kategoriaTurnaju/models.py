from django.db import models
from django.utils.encoding import smart_unicode

from kategoria.models import Kategoria
from turnaj.models import Turnaj 

class KategoriaTurnaju(models.Model):
    turnaj = models.ForeignKey(Turnaj)
    kategoria = models.ForeignKey(Kategoria)
    
    class Meta:
        verbose_name_plural = 'Kategorie Turnajov'
    
    def __str__(self):
        return self.kategoria
    
    def __repr__(self):
        return self.kategoria
    
    def __unicode__(self): 
        return smart_unicode(self.kategoria)