from django.shortcuts import render
from django.http import HttpResponse
from pycricbuzz import Cricbuzz
import json
from .models import Greeting


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def cricket(request):
    c = Cricbuzz();
    matches = c.matches();
    return render(request, json.dumps(matches,indent=4));

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
