from django.views.generic import ListView, DetailView, View, TemplateView
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.shortcuts import render
from buildings.models import property, location, country, province,city
from buildings.forms import *

from django.http import JsonResponse
from .forms import contactus_form

from django.core import serializers
from django.core.mail import send_mail
import requests

def home(request):
    properties = property.objects.all()
    
    all_locations =location.objects.all()

    
    
    #All Possible Location to be displyed ob home search option 
    context = {'properties': properties, 'all_locations':all_locations }  
    return render(request,'principal/index.html',context)



def send_simple_message(msg):

#This methods call the api of MAILGUN. It send the message as a http request rather than SMTP. 


	return requests.post(
		"https://api.mailgun.net/v3/sandboxabeb6a908936437dae6a3556ad8706fc.mailgun.org",
		auth=("api", "8f53fa8cf2662dd96a0690f195aec8ac-2ac825a1-f1fe66f0"),
		data={"from": "mailgun@sandboxabeb6a908936437dae6a3556ad8706fc.mailgun.org",
			"to": ["info@viviendas.art", "lozanojor22@gmail.com"],
			"subject": "Potencial Cliente de ViviendasArt",
			"text": msg })



def contact_us(request):  
    
  
    if request.is_ajax  and request.method == 'POST':
        # wrapped_form = contactus_form(request.POST)    

        # if wrapped_form.is_valid():

    

            
        name =  request.POST['form_name']
        to_email =  request.POST['form_email']
        message =  request.POST['form_message']
        cellphone = request.POST['form_phone']
        complete_message =  "Este mensaje se origino desde la pagina web viviendar.art\n\nNombre de la persona interesada : "+str(name)+ ' \nCorreo Electronico : '+ str(to_email) + ' \nTelefono : '+str(cellphone) + '  \nMensaje : \n'+str(message)

   
        # subject = 'Nuevo mensaje de ViviendasArt'
        # from_email = 'info@viviendas.art' #'my_email@gmail.com' # this is my email 
        # to_email = from_email
        # send_mail (subject, complete_message, from_email,  [to_email], fail_silently=False )

        send_simple_message(complete_message)

       


        #Have to retunrn and ajax SAYING it got sent. 
        return JsonResponse({"valid":True}, status = 200)
    else:
        form = contactus_form()


    return render(request,'principal/contact_us.html',{'form':form})



def about_us(request):      
    context = {}   
    return render(request,'principal/about_us.html',context)

    
def policy(request):
    context = {}   
    return render(request,'principal/privacy_policy.html',context)

    
