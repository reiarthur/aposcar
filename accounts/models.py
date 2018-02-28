from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    UserManager
    )

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        
    username = models.CharField('Nome de usuário', max_length=20, unique=True)
    email = models.EmailField('E-mail', unique=True)
    name = models.CharField('Nome', max_length=100)
    img = models.FileField('Foto de perfil', upload_to='accounts/img')
    is_active = models.BooleanField('Está ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)
    date_joined = models.DateTimeField('Data de cadastro', auto_now_add=True)
    
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    def __str__(self):
        return self.name