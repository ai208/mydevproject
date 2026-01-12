from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class CustomUser(AbstractUser):
    # email はログインに使う
    # null = True にしないとsignupできない。
    email = models.EmailField(unique=True) # ログインようにユニーク
    birthday = models.DateField(null=True,blank=True) # 生年月日
    height = models.IntegerField(null=True, blank=True) # bmiのための身長
    comment = models.TextField(max_length=250,null=True, blank=True) # 自己紹介とか

    #ログインIDをusernameからemailに変更
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    def __str__(self):
        return self.email
