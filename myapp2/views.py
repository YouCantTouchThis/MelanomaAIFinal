from django.shortcuts import render
from .forms import SnippetForm
from .models import Snippet
from django.http import HttpResponseRedirect
import smtplib
import os
from email.message import EmailMessage

import ssl

# Create your views here.
def snippet_detail_view(request):
    form = SnippetForm(request.POST, request.FILES)
    if form.is_valid():
        print("VALID\n\n\n\n")
        form.save()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        #Next, log in to the server
        context = ssl.create_default_context()
        server.starttls(context=context)
        server.login("melanomai.proccess@gmail.com", 'Wowzers!')

        #Send the mail
        msg = EmailMessage()
        
        msg.set_content("""
        Hey there!
        MelanomAI has confirmed your email. We analyzed your image and we detected no Melanoma! Hooray!
        Thanks,
        The MelanomAI Team
        """)
        
        email = form.cleaned_data['email']
        msg["Subject"] = "MelanomAI Email Confirm"
        msg["From"] = 'melanomai.proccess@gmail.com'
        msg['To'] = email


        server.send_message(msg)
        server.quit()
        return HttpResponseRedirect('/thanks/')

        

    context = {'form': form}
    return render(request, 'C:/Users/Sumeet/Melanoma/myapp2/templates/form.html' ,context)

def thanks(request):
    return render(request, 'C:/Users/Sumeet/Melanoma/myapp2/templates/thanks.html')