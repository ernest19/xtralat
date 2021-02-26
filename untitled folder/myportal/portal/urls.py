from django.urls import path
from . import views


app_name = 'portal'


urlpatterns = [
    path('', views.index, name='home'),
    path('indivreport/', views.individualsreport, name='map'),
	path('coreport/', views.cooperatereport, name='map'),
	path('assreport/', views.associationreport, name='map'),
    path('report/', views.report, name='report'),
    path('vcard/', views.vcard, name='vcard'),
    path('managers_details/', views.coperate, name='coperate'),
    path('business_details/', views.coperate2, name='coperate2'),
    path('firm_details/', views.firms, name='firms'),
    path('individual_details/', views.individuals, name='individuals'),
    path('map/', views.map, name='map'),

   

    path('summary/', views.summaryView, name='trainingjson'),

    path('distdetails/', views.dist_details, name='trainingjson'),

   
    path('posdetails/', views.posviews, name='trainingjson'),
    




]