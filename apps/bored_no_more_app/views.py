from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
import requests
from eventbrite import Eventbrite
# HTML-based index method
def index(request):
    return render(request, 'bored_no_more_app/index.html')
def getcategory(request):
    category = request.POST['category']
    location = request.POST['location'].replace(" ","+")
    print category
    print location
    #category = "movies_film"
    #url = "http://eventful.com/oauth/authorize?oauth_token=6ea35d914da91eec8c00"
    url = "http://api.eventful.com/json/events/search?app_key=29hhnm59QqVdfQWf&category=" +category+ "&location=" +location+ "&date=Future&page_size=20"
    #url = "http://api.eventful.com/json/events/search?app_key=29hhnm59QqVdfQWf&category=comedy&location=San+Diego&date=Future&page_size=20"
    # url = "https://www.eventbriteapi.com/v3/events/?token=W5AC5ZM4E7DU3FZLEWHH"
    # notice this is 'requests' not 'request'
    # we are using the requests module 'get' function to send a request from our server
    # then we use ".content" to get the content we are looking for
    response = requests.get(url).content
    # we then send the response back to our template which sent the initial post request
    # we don't jsonify it as it is already in JSON format!
    print "hello"
    return HttpResponse(response, content_type='application/json')
