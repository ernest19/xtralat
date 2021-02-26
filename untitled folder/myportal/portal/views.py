from __future__ import unicode_literals
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from . models import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from djgeojson.views import GeoJSONLayerView
from django.db.models import Sum
from django.db.models import FloatField, Sum
from django.db.models.functions import Cast, Substr
from django.db.models import F ,Q


def index(request):

	# `ld=aa.event_date_field.replace("'" , ""))
		
	return render(request, 'dashboard.html')

def individualsreport(request):
	return render(request, 'individualsreport.html')

def cooperatereport(request):
	return render(request, 'cooperatereport.html')

def associationreport(request):
	return render(request, 'associationreport.html')




	

def report(request):
	return render(request, 'report.html')

def coperate(request):
	return render(request, 'managers_details.html')

def coperate2(request):
	return render(request, 'business_details.html')  

def firms(request):
	return render(request, 'firm_details.html')

def individuals(request):
	return render(request, 'individual_details.html')

def map(request):
	return render(request, 'map.html')


def vcard(request):
	return render(request, 'coperate.html')


def summaryView(request):

	posarr=[]
	sellinarr=[]
	evdarr=[]
	terrarr=[]
	yesarr=[]
	noarr=[]
	momoarr=[]

	if request.GET.get("startdate") and request.GET.get("enddate"):

		terr=TblTraining.objects.filter(event_date_field__gte=request.GET.get("startdate") ,event_date_field__lte=request.GET.get("enddate") ).distinct("territory_id").order_by("territory_id")
		tltmomo=TblTraining.objects.filter(event_date_field__gte=request.GET.get("startdate") ,event_date_field__lte=request.GET.get("enddate")).aggregate(Sum('momo_amount'))["momo_amount__sum"]

		tltevd=TblTraining.objects.filter(event_date_field__gte=request.GET.get("startdate") ,event_date_field__lte=request.GET.get("enddate")).aggregate(Sum('evd_amount'))["evd_amount__sum"]

		tltuser=len(TblTraining.objects.filter(event_date_field__gte=request.GET.get("startdate") ,event_date_field__lte=request.GET.get("enddate")).distinct("user_id"))

		tlstatus=TblTraining.objects.filter(status="Active (Open)",event_date_field__gte=request.GET.get("startdate") ,event_date_field__lte=request.GET.get("enddate")).distinct("user_id").count()


	elif  request.GET.get("startdate"):
		terr=TblTraining.objects.filter(event_date_field__gte=request.GET.get("startdate") ).distinct("territory_id").order_by("territory_id")

		tltmomo=TblTraining.objects.filter(event_date_field__gte=request.GET.get("startdate") ).aggregate(Sum('momo_amount'))["momo_amount__sum"]

		tltevd=TblTraining.objects.filter(event_date_field__gte=request.GET.get("startdate") ).aggregate(Sum('evd_amount'))["evd_amount__sum"]

		tltuser=len(TblTraining.objects.filter(event_date_field__gte=request.GET.get("startdate") ).distinct("user_id"))

		tlstatus=TblTraining.objects.filter(status="Active (Open)",event_date_field__gte=request.GET.get("startdate")).distinct("user_id").count()


	elif  request.GET.get("enddate"):
		terr=TblTraining.objects.filter(event_date_field__lte=request.GET.get("enddate") ).distinct("territory_id").order_by("territory_id")

		tltmomo=TblTraining.objects.filter(event_date_field__lte=request.GET.get("enddate")).aggregate(Sum('momo_amount'))["momo_amount__sum"]

		tltevd=TblTraining.objects.filter(event_date_field__lte=request.GET.get("enddate")).aggregate(Sum('evd_amount'))["evd_amount__sum"]

		tltuser=len(TblUsers.objects.filter(event_date_field__lte=request.GET.get("enddate")).distinct("user_id"))

		tlstatus=TblTraining.objects.filter(status="Active (Open)",event_date_field__lte=request.GET.get("enddate")).distinct("user_id").count()


	else:

		terr=TblTraining.objects.all().distinct("pos__territory").order_by("pos__territory")
		# tltmomo=TblTraining.objects.filter( Q(momo_amount__isnull=False) | ~Q(momo_amount="null")  & ~Q(momo_number__isnull=False) ) .annotate(momo_amount_str=Cast('momo_amount', FloatField())).aggregate(Sum(F('momo_amount_str')))
		tltmomo=TblTraining.objects.filter( ~Q( momo_amount = "null") & ~Q(momo_number__isnull=True) & ~Q( momo_amount = "") ).annotate(momo_amount_str=Cast('momo_amount', FloatField())).aggregate(Sum(F('momo_amount_str')))["momo_amount_str__sum"]

	
		tltevd=TblTraining.objects.all().filter( ~Q( enter_evd_amount = "null") & ~Q(enter_evd_number__isnull=True) & ~Q( enter_evd_amount = "") ).annotate(enter_evd_amount_str=Cast('enter_evd_amount', FloatField())).aggregate(Sum(F('enter_evd_amount_str')))["enter_evd_amount_str__sum"]
		# .aggregate(Sum(F('evd_amount')))["evd_amount__sum"]

		tltuser=len(TblUsers.objects.all().distinct("id"))

		tlstatus=TblUsers.objects.filter(status="active").distinct("id").count()

		territ= Territories.objects.all()
		users=TblPos.objects.all().distinct("pos")


	
	
	for aa in territ:

		pos=TblTraining.objects.filter(pos__territory=aa.territoryid).count()

		yes=TblTraining.objects.filter(pos__territory=aa.territoryid , knowledge_of_selling_products=1).count()
		no=TblTraining.objects.filter(pos__territory=aa.territoryid , knowledge_of_selling_products=0).count()

		evd=TblTraining.objects.filter( ~Q( enter_evd_amount = "null") & ~Q(enter_evd_number__isnull=True) & ~Q( enter_evd_amount = "") ,pos__territory=aa.territoryid ).annotate(enter_evd_amount_str=Cast('enter_evd_amount', FloatField())).aggregate(Sum(F('enter_evd_amount_str')))["enter_evd_amount_str__sum"]

		momo=TblTraining.objects.filter( ~Q( momo_amount = "null") & ~Q(momo_number__isnull=True) & ~Q( momo_amount = "") , pos__territory=aa.territoryid ).annotate(momo_amount_str=Cast('momo_amount', FloatField())).aggregate(Sum(F('momo_amount_str')))["momo_amount_str__sum"]

		terrarr.append(aa.territoryid)
		posarr.append([aa.territoryid , pos])
		yesarr.append(yes)
		noarr.append(no)
		evdarr.append(checknone(evd))
		momoarr.append(checknone(momo))


	# print(posarr)
	# print(sellinarr)
	# print(evdarr)
	return render(request, 'summary.html',locals())



def posviews(request):



	users=TblTraining.objects.filter(pos=request.GET.get("pos"))[:10]
	for aa in users:
		print(aa.momo_amount)



	return render(request, 'posdetails.html',locals())







def dist_details(request):
	arr=[]
	distcode = request.GET.get("dist")
	county=County.objects.get(id=distcode)
	pos=TblTraining.objects.filter(geom__within=county.geom).distinct("category")
	for aa in pos :
		poscount=TblTraining.objects.filter(category= aa.category ,geom__within=county.geom).count()
		arr.append([aa.category,poscount])
	print(arr)
	return render(request, 'distdetails.html' , locals())






def checknone(data):
	if data == None:
		return 0
	else:
		return data












