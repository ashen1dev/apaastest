import os
import requests
import time
from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting


# Create your views here.
def index(request):
    times = int(os.environ.get('TIMES',3))
    start = time.time()
    sum = 0
    for i in range(1, 100000000):
        sum = sum + i
    elapsed = time.time() - start
    temp = HttpResponse('Hello! '+ str(elapsed))
    return temp

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
