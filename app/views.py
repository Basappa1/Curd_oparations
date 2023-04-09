from django.shortcuts import render

# Create your views here.
from app.models import *

def Display_Access(request):
    LOT=AccessRecord.objects.all
    
    LOT=AccessRecord.objects.filter(author='Ronaldo Kumar')
    LOT=AccessRecord.objects.exclude(author='Naveen')
    LOT=AccessRecord.objects.all().order_by('name')#asce
    LOT=AccessRecord.objects.all().order_by('-name')#desc
    LOT=AccessRecord.objects.all().order_by(Length('name'))
    
    
    
    a={'LOT':LOT}
    return render(request,'AccessRecord.html',a)



def Webpage_dispay(request):
    LOW=Webpage.objects.all()
    b={'LOW':LOW}
    return render(request,'Webpage_display.html',b)

