from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from Accounts.models import User
from django.conf import settings


#helper function
def mailresetpassword(request,user):
    from_email = settings.DEFAULT_FROM_EMAIL
    current_site = get_current_site(request) #this current sites should be changed once it go-live. now it is local site
    mailSubject = 'Please reset your password from following link'
    message = render_to_string('Accounts/resetpasswordlink.html',
    {'user':user,
    'domain':current_site,
    'uid':urlsafe_base64_encode(force_bytes(user.pk)), #to send this pk of user with secure encode it with this func
    'token':default_token_generator.make_token(user),
    })

    to_email = user.email
    mail = EmailMessage(mailSubject,message,from_email,to=[to_email])
    mail.send()