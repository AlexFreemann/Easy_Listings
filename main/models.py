from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.


class Account(models.Model):

    user=models.OneToOneField(User, on_delete=models.CASCADE)
    email=models.EmailField('Email')
    shop_name=models.CharField('Shop', max_length=20,blank=True,default=None)
    password = forms.CharField(widget=forms.PasswordInput)
    shop_connection=models.BooleanField('Shop Connection',default=False)
    paid = models.BooleanField('Payment',default=False)
    verified = models.BooleanField('Verification', default=False)



    def __str__(self):
        return self.user.username