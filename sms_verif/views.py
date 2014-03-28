#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from sms_verif.forms import Code
from accounts.models import MyProfile,GeoLocation1,GeoLocation2,Code_db,Reputation

def code(request):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = Code(request.POST)  # Nous reprenons les données
        if form.is_valid(): 
            # Ici nous pouvons traiter les données du formulaire
            verif_num = form.cleaned_data['verif_num']
            obj = Code_db.objects.latest('sav_date')
            ph = MyProfile.objects.get(id=obj.client_id)
            loc1 =  GeoLocation1.objects.get(client_id=obj.client_id)
            loc2= GeoLocation2.objects.filter(client_id=obj.client_id).order_by('-id')[0]
            #loc2 =  GeoLocation2.objects.get(client_id=obj.client_id)
            if loc1.country == loc2.country:
                verif_country = False
            else: verif_country = True

            if verif_num==obj.code:
                verif_code = False
            else: verif_code = True
            cal = 0.3*verif_country+07*verif_code
            rep = Reputation(client=ph, verif_code_doesntMatch=verif_code, country_doesntMatch=verif_country ,proxy_detect="default", score=cal)
            rep.save()
            if verif_num==obj.code:
                return HttpResponseRedirect('/accounts/')
        return HttpResponseRedirect('/accounts/signin')
    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = Code()  # Nous créons un formulaire vide
    return render(request, 'verif/code.html', locals())
