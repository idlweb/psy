from django.shortcuts import render
from django.template import Template, Context

def demopsy(request):
    # View code here...



    return render(request, 'frontend/index.html', {
        'base': 'esempio',
    }, content_type='application/xhtml+xml')