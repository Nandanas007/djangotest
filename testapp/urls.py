from django.urls import path #type:ignore
from . import views
urlpatterns=[
    path('sample/',views.sample,name='sample'),
]