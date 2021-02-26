from django.urls import path
from . import views

app_name = 'rootApp'

urlpatterns = [
   
	path('', views.mapView, name='map'),    

	path('trainingjson/', views.Training4326Layer, name='trainingjson'),

	path('regionjson/', views.RegionLayer.as_view(), name='trainingjson'),

	path('countyjson/', views.countyLayer.as_view(), name='trainingjson'),
	path('heatmap/', views.heatmapView, name='trainingjson'),


  	
 ]

