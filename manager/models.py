from django.db import models
import os
# Create your models here.

class SoftwarePackage(models.Model):
    name = models.CharField('软件名', max_length=200)
    author = models.CharField('作者', max_length=100)
    pub_house = models.CharField('来源机构', max_length=200)
    pub_date = models.DateTimeField('date published')
    file = models.CharField('申请软件包', max_length=300, default='')
    status = models.CharField('状态', max_length=10, default='')