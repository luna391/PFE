#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from sms_verif.forms import Code
from accounts.models import MyProfile,Location,Code_db

def code(request):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = Code(request.POST)  # Nous reprenons les données
        if form.is_valid(): 
            # Ici nous pouvons traiter les données du formulaire
            verif_num = form.cleaned_data['verif_num']
            obj = Code_db.objects.latest('sav_date')
            if verif_num==obj.code:
                return HttpResponseRedirect('/accounts/')

        return HttpResponseRedirect('/accounts/signin')

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = Code()  # Nous créons un formulaire vide

    return render(request, 'verif/code.html', locals())
