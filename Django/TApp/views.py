from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test2(request):
    return HttpResponse("This has worked")

# this allows us to see HTML content on the website
def test(request):
    return render(request, 'base.html', { 'name' : 'aaron'})