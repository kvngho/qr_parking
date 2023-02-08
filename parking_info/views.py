from django.shortcuts import render
from .models import ParkingInformation
# Create your views here.

def detail_page(request, key):
    object = ParkingInformation.objects.get(key=key)
    context = {'parking_info': object}
    return render(request, 'calling-test.html', context)

