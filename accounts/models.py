
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Activation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(verbose_name=_('First name'), max_length=255,blank=True,default=f'first name')
    last_name = models.CharField(verbose_name=_('Last name'), max_length=255,blank=True,default=f'last name')
    image = models.ImageField(default='profile/not-pictured-circle.png',upload_to='profile/custom')

    def __str__(self):
        return f'{self.user.username} image profile'

