
from django.shortcuts import render
from . models import place
from . models import team


def demo(request):
    obj = place.objects.all()
    obj1= team.objects.all()
    return render(request,"index.html",{'result':obj,'team':obj1})
def contact(request):
    return render(request,"contact.html")
def destinations(request):
    return render(request,"destinations.html")
def elements(request):
    return render(request,"elements.html")
def news(request):
    return render(request,"news.html")
def about(request):
    return  render(request,"about.html")