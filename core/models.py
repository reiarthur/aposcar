from django.db import models
#from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
#from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model


#TROCAR GENERIC RELATION PARA CATEGORIA

# Create your models here.
class Category(models.Model):
    
    CATEGORY_TYPES = (
        ('D', 'Director'),
        ('M', 'Movie'),
        ('A', 'Actor'),
        ('S', 'Song')
        )
        
    name = models.CharField('Nome', max_length=100)
    category_type = models.CharField('Tipo', max_length=1, choices=CATEGORY_TYPES)
    
    def __str__(self):
        return self.name

class Nominee(models.Model):
    
    NOMINEE_TYPES = (
        ('D', 'Director'),
        ('M', 'Movie'),
        ('A', 'Actor'),
        ('S', 'Song')
        )
    
    name = models.CharField('Nome', max_length=100)
    img = models.FileField('Foto', upload_to='nominees/img')
    nominee_type = models.CharField('Tipo', max_length=1, choices=NOMINEE_TYPES)
    
    def __str__(self):
        return self.name
        
        
class Bet(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    #content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    #object_id = models.PositiveIntegerField()
    #content_object = GenericForeignKey()
    nominee = models.ForeignKey(Nominee, on_delete=models.CASCADE, null=True)
    
    created_at = models.DateTimeField('Data da aposta', auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'category')
        
    def __str__(self):
        return "%s apostou em %s para %s" % (self.user, self.nominee, self.category)

"""class Director(models.Model):
    name = models.CharField('Nome', max_length=100)
    img = models.FileField('Foto', upload_to='directors/img')
    bet = GenericRelation(Bet, related_query_name='directors')
    
    def __str__(self):
        return self.name
    

class Movie(models.Model):
    title = models.CharField('Titulo', max_length=100)
    img = models.FileField('Poster', upload_to='movies/img')
    bet = GenericRelation(Bet, related_query_name='movies')
    
    def __str__(self):
        return self.title

class Actor(models.Model):
    name = models.CharField('Nome', max_length=100)
    img = models.FileField('Foto', upload_to='actors/img')
    bet = GenericRelation(Bet, related_query_name='actors')
    
    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField('Titulo', max_length=100)
    img = models.FileField('Cover', upload_to='songs/img')
    bet = GenericRelation(Bet, related_query_name='songs')
    
    def __str__(self):
        return self.title"""

# https://simpleisbetterthancomplex.com/tutorial/2016/10/13/how-to-use-generic-relations.html