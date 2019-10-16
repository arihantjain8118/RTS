from django.shortcuts import render
from .models import Train, Ticket
from django.template.loader import render_to_string
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from .forms import ticket


# Create your views here.
def starting(request):
    user=request.user
    print("jdcncj")
    return render(request,'home/starting.html',{'user':user})

def trains(request):
    if request.is_ajax():
        print("aaya")
        source = request.POST.get('source',None)
        destination = request.POST.get('destination',None)
        date = request.POST.get('date',None)
        print(source)
        print(destination)
        print(date)
        trains=[]
        ptrains = (Train.objects.filter(source__iexact=source))
        for i in ptrains:
            print(i.destination.upper())
            if(i.destination.upper() == destination.upper()):
                trains.append(i)

        context={'trains':trains}
        html = render_to_string('home/trains.html',context,request=request)
        return JsonResponse({'form': html})

def ticketbook(request,id):
    train = Train.objects.filter(id=id).first()
    return render(request,'home/book.html',{'train':train})

def ticketbk(request):
    form = ticket()
    return render(request,'home/tick.html',{'form':form})