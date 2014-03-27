from django.db import models
from django.contrib.auth.models import User  
from django.utils.translation import ugettext as _  
from userena.models import UserenaBaseProfile  

class MyProfile(UserenaBaseProfile):  
    user = models.OneToOneField(User,unique=True,  
                        verbose_name=_('user'),related_name='my_profile')
    phone = models.CharField(max_length=12)

class GeoLocation1(models.Model):
    client = models.ForeignKey(MyProfile)
    ip = models.GenericIPAddressField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    proxy = models.BooleanField()


class GeoLocation2(models.Model):
    client = models.ForeignKey(MyProfile)
    ip = models.GenericIPAddressField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    proxy = models.BooleanField()

class Code_db(models.Model):
    client = models.ForeignKey(MyProfile)
    code = models.CharField(max_length=6)
    sav_date = models.DateTimeField()

class Reputation(models.Model):
    client = models.ForeignKey(MyProfile)
    #assword_doesntmatch = models.BooleanField()
    verif_code_doesntMatch = models.BooleanField()
    country_doesntMatch = models.BooleanField()
    proxy_detect = models.BooleanField()
    score = models.IntegerField()


  
