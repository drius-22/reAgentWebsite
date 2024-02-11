from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import property, location, country, province,city
from django.db.models import Q
from .forms import RequestVisit
from django.core import serializers
from django.core.mail import send_mail
from django.template.loader import render_to_string
# from django.views.decorators.csrf import csrf_exempt


import requests
import datetime
import smtplib
# If something fails always return an error page 




def send_simple_message(msg):

#This methods call the api of MAILGUN. It send the message as a http request rather than SMTP. 

	return requests.post(
		"https://api.mailgun.net/v3/sandbox5429e5c71eb141a1a8a7f16ce8876a07.mailgun.org/messages",
		auth=("api", "59e8dbf05f0798652de3ab9ac53182ca-a3c55839-0fb423c3"),
		data={"from": "mailgun@sandbox5429e5c71eb141a1a8a7f16ce8876a07.mailgun.org",
			"to": ["info@viviendas.art", "lozanojor22@gmail.com"],
			"subject": "Posible Cliente de ViviendasArt",
			"text": msg })


def agent_request(request):  
 

    if request.is_ajax  and request.method == 'POST':
        # # wrapped_form = contactus_form(request.POST)    

        # # if wrapped_form.is_valid():

            
        name =  request.POST['request_name']
        to_email =  request.POST['request_email']
        message =  request.POST['request_message']
        cellphone = request.POST['request_phone']
        complete_message =  "Este mensaje se origino desde la pagina web viviendar.art\n\nNombre de la persona interesada : "+str(name)+ ' \nCorreo Electronico : '+ str(to_email) + ' \nTelefono : '+str(cellphone) + '  \nMensaje : \n'+str(message)

        # subject = 'Nuevo mensaje de ViviendasArt'
        # from_email = 'info@viviendas.art' #'my_email@gmail.com' # this is my email 
        # to_email = from_email
        # send_mail (subject, complete_message, from_email,  [to_email], fail_silently=False )

        send_simple_message(complete_message)
     

        #Have to retunrn and ajax SAYING it got sent. 
        return JsonResponse({"valid":True}, status = 200)

    else:
        return JsonResponse({"valid":False}, status = 200)
   



def property_view(request, pk):
    """
        displays individual properties
    """
   
    form = RequestVisit()
    property_e = property.objects.get(pk=pk)
    features = property_e.features.split(',')
    features =[ feature.strip().casefold().capitalize()   for feature in features ]

    last_three = property.objects.filter(~Q(pk=pk)).filter(category=property_e.category).order_by('date_posted')[:3]
    testing =  last_three.first()       
    context = {'property':property_e,'features': features, 'last_three': last_three, 'form':form}
    #context = {'property':property_e,'features': features, 'last_three': last_three}

    return render (request, 'buildings/single_property_2.html',context)
        
    # except property_view.DoesNotExist:
    #     context ={}
    #     return render (request, 'extra/404.html',context)






def show_properties(request, status):
    """
        Redirects as hard coded links. Used from home and menu bar 
    """
    try:
        status = status.lower()
        if status == 'renta' or status == 'venta' :
            properties = property.objects.filter(type=status)
        else :
            properties = property.objects.all()

        

        context = {'properties': properties}
        context['type_of']= status.capitalize()


        all_locations =location.objects.all() # can be joined in method with serch_properties
        # context['all_locations']= all_locations

        context['all_locations']= None 

        # return render (request, 'buildings/properties_List.html', context)
        return render (request, 'buildings/properties-grid-2.html', context)
    except property.DoesNotExist:
        context ={}
        return render (request, 'extra/404.html',context)






def search_properties(request):

    context ={}


    if request.method == "POST":

        location_pk   = request.POST['search-property-location']# pk of the location table 
        property_type = request.POST['search-property-type']   # casa, apartamento, terreno
        status        = request.POST['search-property-status'] #venta o renta
        n_baths       = request.POST['search-property-bathrooms']
        n_beds        =  request.POST['search-property-bedrooms']
        
        location_pk   = int(location_pk) if location_pk else  1 # default randomly selected 
        property_type = property_type if property_type else 'casa' # default randomly selected 
        status        = status if status else 'venta'
        n_baths       = int(n_baths) if n_baths else 0 # default is very small number since will try to find n_baths or more
        n_beds        = int(n_beds) if n_beds else 0 # 
       
        #I'm not filtering by price nor by size yet ( these are not input tags so is more diffucult)
        # price         = 10000000 # very big value. i am not filtering by price FOR now (all properties are meant to pass this filter)
        # size          = 

        filtered_properties = property.objects.filter(location=location_pk, category=property_type,  type=status, n_bathrooms__gte=n_baths,  n_bedrooms__gte=n_beds )
        
        context['properties']= filtered_properties

     



        all_locations = location.objects.all() # can be joine din 1 method with show_properties
        context['all_locations'] = all_locations

        

        return render (request, 'buildings/properties_List.html', context )
        


    return render (request, 'extra/404.html',context)


# def for_sale(request):
#     properties = property.objects.all()
#     context = {'properties': properties}
#     return render (request, 'buildings/grid_properties.html',context)

# def for_rent (request):
#     properties = property.objects.all()
#     context = {'properties': properties}
#     return render (request, 'buildings/properties_List.html',context)    