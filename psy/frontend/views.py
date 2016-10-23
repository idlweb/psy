from django.shortcuts import render
from django.template import Template, Context
from .forms import noFS_Form
from django.http import HttpResponseRedirect

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
        form = form_class(request.POST)
        #form = ArticleForm()
	

    return render(request, 'psy/frontend/index.html', { 'base': 'esempio', 'form': form })
