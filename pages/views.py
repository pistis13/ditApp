from django.shortcuts import render

def homepage( request ) :
    return render( request, "index.html")

def aboutUsPage( request ):
     return render(request, "about.html")

def servicePage( request ):
     return render(request, "services.html")

def serviceDetailsPage( request ):
     return render(request, "services-detail.html")

def newsPage( request ):
     return render( request, "news.html") 
def newsDetailsPage( request ):
     return render( request, "news-details.html")