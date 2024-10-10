from django.shortcuts import render #type:ignore
from django.http import HttpResponse #type:ignore
def sample(request):
    msg="<h1>Sample django project</h1>"
    msg+="<p>This is my first django project in github </p>"
    return HttpResponse(msg)

# Create your views here.
