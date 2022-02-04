import time
from django.http import HttpResponse
from django.shortcuts import render
from .tasks import countdown

# Create your views here.
def index(request):
    start = time.time()
    countdown.apply_async()
    return HttpResponse(f"Returned in {time.time() - start} seconds")
