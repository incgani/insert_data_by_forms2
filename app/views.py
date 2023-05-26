from django.shortcuts import render
from app.models import *

# Create your views here.
def i_topic(request):
    if request.method=='POST':
        tn=request.POST.get('topi')
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
    return render(request,'wtopic.html')

def i_webpage(request):
    LTO=Topic.objects.all()
    d={'webpage':LTO}

    if request.method=='POST':
        topic=request.POST['topic']
        name=request.POST['name']
        url=request.POST['url']
        email=request.POST['email']
        TO=Topic.objects.get(topic_name=topic)
        WO=WebPage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)[0]
        WO.save()
    return render(request,'wwebpage.html',d)

def i_access(request):
    WLO=WebPage.objects.all()
    d={'access':WLO}
    if request.method=='POST':
        name=request.POST['name']
        author=request.POST['author']
        date=request.POST['date']
        WO=WebPage.objects.get(name=name)
        AR=AccessRecords.objects.get_or_create(name=WO,author=author,date=date)[0]
        AR.save()
    return render(request,'waccess.html',d)

def retrevied(request):
    return render(request,'wretrevied.html')
