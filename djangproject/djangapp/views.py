from django.shortcuts import render
from . models import sake
from . models import lake
# Create your views here.
def pep(request):
    ars = sake.objects.all()
    brs = lake.objects.all()
    return render(request, 'index.html', {'result': ars,'res': brs})

