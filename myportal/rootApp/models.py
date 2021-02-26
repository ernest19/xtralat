# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#Have Updated the usertbl with the AbstractBaseUser
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.gis.db import models
from django.contrib.auth.models import User


# Create your models here.
#/// Web Forms /////////////////////////////////////////////////////////////////////////////////
class timeStamp(models.Model):
	"""
	Description: This models is an abstract class that defines the columns that should be present in every table.
	"""
	created_date = models.DateTimeField(auto_now=True)
	delete_field = models.CharField(max_length=10, default="no")


	class Meta:
		abstract = True



class ProtectedArea(models.Model):
    id = models.IntegerField(primary_key=True)
    geom = models.GeometryField(blank=True, null=True)
    reserve_na = models.CharField(max_length=30, blank=True, null=True)
    region = models.CharField(max_length=30, blank=True, null=True)
    area_sqkm = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Protected Area'


class RegionalBoundary2019(models.Model):
    id = models.IntegerField(primary_key=True)
    geom = models.GeometryField(blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Regional_Boundary_2019'


class District(models.Model):
    id = models.IntegerField(primary_key=True)
    geom = models.GeometryField(blank=True, null=True)
    created_da = models.CharField(max_length=254, blank=True, null=True)
    delete_fie = models.CharField(max_length=10, blank=True, null=True)
    district_n = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=10, blank=True, null=True)
    region = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'district'


class Forestry(models.Model):
    geom = models.GeometryField(blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    area = models.CharField(max_length=10, blank=True, null=True)
    north = models.CharField(max_length=15, blank=True, null=True)
    west = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forestry'
