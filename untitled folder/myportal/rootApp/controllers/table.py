from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#This session handles all the function for table paginations



def model_table(request, modelname, tableheaderdict, filterquery = {}, paginations = 10):
	"""
		request 
		modelname refer to the table model name
		tableheaderdict refer to the table header name in dict format {}
		filterquery refer to the queryfilter in dict format {}
		will return list of table
	"""

	modeltable = modelname.objects.filter(delete_field='no', **filterquery)
	paginator = Paginator(modeltable, paginations, 1)

	page = request.GET.get('page')
	try:
		list_table = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		list_table = paginator.page(1)
	except EmptyPage:
		list_table = paginator.page(paginator.num_pages)
        # If page is out of range (e.g. 9999), deliver last page of results.
        


	return list_table


# def export_to_csv(modeltable, filtertypename):
# 	response = HttpResponse(content_type='text/csv')
# 	response['Content-Disposition'] = 'attachment; filename="' + filtertypename + '.csv"'
# 	ignore_field = ['delete_field']
	
# 	for m in modeltable:
# 		sear.append(m[0])
# 		sear1.append(m[1])
# 	writer = csv.writer(response)
	
				
# 	writer.writerow(sear1)
# 	#	break
	
# 	for obj in tablelist:
# 		rows = []
# 		for keys in obj:
# 			rows.append(definevalue(keys))

# 		writer.writerow(rows)

#    	return response
