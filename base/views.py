from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from django.utils import timezone
from rest_framework.decorators import api_view
from datetime import timedelta
from .helper import api

# Create your views here.


def index(request):
    return render(request, 'index.html')


@api_view(['GET', 'POST'])
def api_response(request):
    if request.method == 'POST':
        lat = float(request.POST.get('latitude'))
        lon = float(request.POST.get('longitude'))
        typ = request.POST.get('type')
        currenttime = timezone.now()
        diff_time = timedelta(minutes=10)
        try:
            filt = Weather.objects.get(
                latitude=lat, longitude=lon, detailing=typ)
        except:
            filt = None
        if filt:
            if ((currenttime-filt.date) < diff_time):
                print("from db")
                return Response(filt.response)
            else:
                print("from Db and updated")
                response = api(lat, lon, typ)
                filt.respone = response.json()
                filt.save()
                return Response(response.json())
        else:
            print("From api")
            response = api(lat, lon, typ)
            weather = Weather.objects.create(
                latitude=lat, longitude=lon, detailing=typ, response=response.json())

        return Response(response.json())
