from django.shortcuts import render
from django.http import HttpResponse
from contact.models import  Contact 
from blog.models import Yangiliklar
from django.contrib.auth import authenticate, login



def blog(request):
    yangilik = Yangiliklar.objects.all()
    context = {'yangilik': yangilik}
    return render(request, 'blog.html', context)



def index(request):
    return render( request, "index.html")

def about(request):
    return render( request, "about.html")



def services(request):
    return render( request, "services.html")


def contact(request):
    if request.method == "POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        messages=request.POST.get('messages')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.messages=messages
        contact.save()
        return HttpResponse("<h1> ok </h1>")
    return render(request, 'contact.html')
        
def blog(request):
    return render( request, "blog.html")