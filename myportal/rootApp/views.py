# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import ast
# import datetime, pdfkit, random, os, calendar
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
# from django.contrib.auth import authenticate, login , logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
# from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.gis.geos import GEOSGeometry
# from django.http import JsonResponse, HttpResponse, StreamingHttpResponse
from djgeojson.views import GeoJSONLayerView
from django.contrib.gis.db.models import Extent
from django.core.serializers import serialize
from portal.models import *
from datetime import date
today = date.today()


def rootView(request):
    toHTML  ={}

    return render(request, 'rootApp/landing.html', toHTML)



def mapView(request):
    toHTML  ={}

    return render(request, 'rootApp/map.html', toHTML)



def AutocompleteView(request):
  data = RegionalBoundary2019.objects.filter(region__icontains = request.GET['phrase'])
  data1 = []
  n = 0
  
  for s in data:
    sname = str(s.region)
    sname = sname.title()
    data1.append({'code':str(s.id),'name':sname , 'type' : 'region'})

  data =  District.objects.filter(district_n__icontains = request.GET['phrase'])[:10]
  for s in data:
    sname = str(s.district_n)
    sname = sname.title()
    data1.append({'code':str(s.district),'name':sname , 'type' : 'district'})

  data =  Forestry.objects.filter(name__icontains = request.GET['phrase'])[:10]
  for s in data:
    sname = str(s.name)
    sname = sname.title()
    data1.append({'code':str(s.id),'name':sname , 'type' : 'plantation'})
  return JsonResponse(data1, safe=False)


def ExtentView(request, valuecode=None, ftype=None):
  toHTML = {}

  try:
    if ftype == 'region':
      tojson = RegionalBoundary2019.objects.filter(id=valuecode).aggregate(Extent('geom')).get('geom__extent')
      # print tojson
    elif ftype == 'district':
      tojson = District.objects.filter(district=valuecode).aggregate(Extent('geom')).get('geom__extent')

    elif ftype == 'plantation':
   
      tojson = Forestry.objects.filter(id=valuecode).aggregate(Extent('geom')).get('geom__extent')
      
  except Exception as e:
    raise


  return JsonResponse(tojson,safe = False)




def heatmapView(request):
  arr=[]
  pos=TblTraining.objects.all()
  for aa in pos :
    heat={}
    heat["lat"]=aa.latitude
    heat["lng"]=aa.longitude
    
    arr.append(heat)
  return JsonResponse(arr , safe = False)




def Training4326Layer(request):
  resulpoygon = []

  date= today.strftime("%Y-%m-%d")

  dist=TblTraining.objects.all()
  # filter(event_date__date=date)

  for aa in dist:
    properties={}
    properties['owner_first_name']=aa.pos.owner_first_name
    properties['owner_last_name']=aa.pos.owner_last_name
    properties['business_name']=aa.pos.business_name
    properties['category']=aa.pos.category
    properties['status']=aa.pos.status
    if aa.geom:
      resulpoygon.append({"geometry":ast.literal_eval(returnsimplify(aa.geom)),"type":"Feature","properties":properties,"id":str(aa.id)})
  return JsonResponse(resulpoygon,safe=False)

def topolygon(resulpoygon):
  mainjson = []
  mainjson.append({"crs":{"type":"link","properties": {"href":"http://spatialreference.org/ref/epsg/4326/","type":"proj4"}},"type":"FeatureCollection","features":resulpoygon})
  return mainjson



def returnsimplify(geom,simplifyvalue=0.001):
  # return geom.simplify(simplifyvalue, preserve_topology=True).geojson
  return geom.simplify(simplifyvalue).geojson



def returnsimplify1(geom,simplifyvalue=0):
  # return geom.simplify(simplifyvalue, preserve_topology=True).geojson
  return geom.simplify(simplifyvalue).geojson




class RegionLayer(GeoJSONLayerView):
  # Options
  model = RegDist  #.objects.filter(region_new='GREATER ACCRA')
  precision = 3   
  simplify = 0.001
  properties = ('name')


class countyLayer(GeoJSONLayerView):
  # Options
  model = Territories  #.objects.filter(region_new='GREATER ACCRA')
  precision = 3   
  simplify = 0.001
  properties = ('territoryname')

