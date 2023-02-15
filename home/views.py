from django.shortcuts import render
from .models import Apps, Client, Dest, Goal, Mission, Objective, Portfolio, Slide, Weps, Wep1

# Create your views here.



def index(request):
    
    client = Client.objects.all()
    ordering=['-created']
    #code for index slide 
    
    object = Objective.objects.all()
    ordering = ['-created']
    
    go = Goal.objects.all()
    ordering = ['-created']
    
    dest = Dest.objects.all()
    ordering=['-created']
    
    portfolio = Portfolio.objects.all()
    ordering=['-created']
    
    slide = Slide.objects.all()
    ordering=['-created']
    
    mission = Mission.objects.all()
    ordering=['-created']
    
    app = Apps.objects.all()
    ordering=('-id')
    
    wep = Weps.objects.all()
    ordering = ('-id')

    card = Wep1.objects.all()
    ordering = ('-id')
    
    return render(request, "index.html" ,{'client':client, 'dest':dest ,'slide':slide, 'mission':mission, 'portfolio':portfolio, 'app':app, 'wep':wep, 'card':card, 'object':object, 'go':go})


def portfolio(request):
    
    portfolio = Portfolio.objects.all()
    ordering=['-created']
    
    
    
    app = Apps.objects.all()
    ordering=('-id')
    
    wep = Weps.objects.all()
    ordering = ('-id')

    card = Wep1.objects.all()
    ordering = ('-id')
    
    
    return render(request, "portfolio.html" ,{'portfolio':portfolio ,'app':app, 'wep':wep, 'card':card}) 


def portfolioDetails(request):
    
    return render(request, "portfolio-details.html")

def services(request):
    
    
    return render(request, "services.html")