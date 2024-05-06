from django.urls import path
from . import views

urlpatterns = [
    path("",views.homepage ),
    path("about/",views.aboutUsPage),
    path("service/",views.servicePage ),
    path("service/detail",views.serviceDetailsPage),
    path("news/",views.newsPage),
    path("news/details",views.newsDetailsPage)
]
