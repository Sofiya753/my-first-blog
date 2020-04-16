from django.urls import  path, include
from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from ad.models import Ad
urlpatterns = [

    path('',ListView.as_view(queryset=Ad.objects.all().order_by("title")[:20],
    template_name="ad/ad.html")),
    url('^(?P<pk>\d+)$' , DetailView.as_view(model=Ad, template_name="ad/oneAd.html"))
]
