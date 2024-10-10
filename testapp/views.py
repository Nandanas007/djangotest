from django.shortcuts import render #type:ignore
from django.http import HttpResponse #type:ignore
from django.template import loader  #type:ignore
def sample(request):
    msg="<h1>Sample django project</h1>"
    msg+="<p>This is my first django project in github </p>"
    return HttpResponse(msg)
def page2(request):
    tmp=loader.get_template('index.html')
    return HttpResponse(tmp.render())

# Create your views here.
