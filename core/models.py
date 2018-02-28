from django.db import models
from django.contrib.auth import get_user_model


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
    nominee = models.ForeignKey(Nominee, on_delete=models.CASCADE, null=True)
    
    created_at = models.DateTimeField('Data da aposta', auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'category')
        
    def __str__(self):
        return "%s apostou em %s para %s" % (self.user, self.nominee, self.category)
