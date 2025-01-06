from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# from django.views.decorators.http import require_http_methods, require_GET, require_POST

# Create your views here.
events = [
    {
    "id":"1", 
     "title":'first event', 
     "date":"2017/2/2"
     },
       {
    "id":"1a", 
     "title":'second event', 
     "date":"2017/3/2"
     },

]
def index(request):
    if request.method == 'GET':
        return JsonResponse(events, safe=False) #json response expects dictionary data by default

def create(request):
    if request.method == 'POST':
        return HttpResponse("event created successfully")

def getById(request, id):
    if request.method == 'GET':
        return HttpResponse(f"event with id {id} has following details")

def updateById(request, id):
    if request.method == 'PATCH':
        return HttpResponse(f"event with id {id} updated successfully")

def deleteById(request, id):
    if request.method == 'DELETE':
        return HttpResponse(f"event with id {id} deleted successfully")

