from django.shortcuts import render
from django.template import Template, Context
from .forms import *
from django.http import HttpResponseRedirect
from django.forms import fields, models, formsets, widgets

from allauth.socialaccount.models import SocialToken
from django.contrib.auth.models import User

from allauth.socialaccount.tests import OAuth2TestsMixin
from allauth.account import app_settings as account_settings
from allauth.account.models import EmailConfirmation, EmailAddress
from allauth.socialaccount.models import SocialAccount, SocialToken
from allauth.tests import MockedResponse, TestCase, patch
from allauth.account.signals import user_signed_up
from allauth.account.adapter import get_adapter
from requests.exceptions import HTTPError

"""--------------------
url(r'^accounts/profile/', direct_to_template, { 'template' : 'profile.html' }),
--------------------"""


"""--------------------
from django.dispatch import receiver
from allauth.socialaccount.signals import pre_social_login

@receiver(pre_social_login)

def populate_profile(sender, **kwargs):
    u = UserProfile( >>FACEBOOK_DATA<< )
    u.save()
-----------------------"""


#https://api.linkedin.com/v1/people/~?oauth2_access_token=AQXg0HjK69GGG8x0gmSiAylmcUOGDzs8ocOtM-crdb1AKUHZ121G9iDNqZKKatk-yDyhjtXzMMT4gptT55I3_vKAcgMeiByP0NTnedxTuQicWJPho2SyPx1S6PO2XUKu0bcppssuok761ZpwQSlJwGtSRhyGovrG6uBC02l8RPNink9ryHQ&format=json

"""---"""

#user = get_user_model()
#account = User.socialaccount_set.get(provider="linkedin")
#refresh_token = account.socialtoken_set.first().token_secret
#SocialToken.objects.filter(account__user=user, account__provider='linkedin')


def demopsy(request):
    # View code here...
    # if this is a POST request we need to process the form data
    form_class = noFS_Form
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = form_class(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/admin/')

    # if a GET (or any other method) we'll create a blank form

    else:
        form = form_class()
        #form = ArticleForm()

    user = request.user
	
    #access_token = SocialToken.objects.get(account__user=request.user, account__provider='linkedin_oauth2') #get instead of filter (you need only one object)

    #account = user.socialaccount_set.get(provider="linkedin_oauth2")   

    #refresh_token = account.socialtoken_set.first().token_secret

    return render(request, 'psy/frontendpsy/index.html', { 'base': 'esempio', 'form': form, 'token':'ok' })


def bank(request):
    form_class = BankForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/bank/')
    else:
        form = form_class()
    return render(request, 'psy/frontendpsy/demo_bank.html', { 'base': 'esempio', 'form': form })



