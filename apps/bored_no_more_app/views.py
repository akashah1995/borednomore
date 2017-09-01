from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
import bcrypt
import requests
# HTML-based index method

def intro(request):
    return render(request, 'bored_no_more_app/intro.html')

def index(request):
    return render(request, 'bored_no_more_app/index.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags = tag)
        return redirect(intro)
    else:
        firstname = request.POST['firstname']
        username = request.POST['username']
        email = request.POST['email']
        password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        print firstname, username, email, password
        User.objects.create(firstname = firstname, username = username, email = email, password = password)
        user = User.objects.get(username = username)
        request.session['loggedIn'] = user.id

        return redirect(index)

def login(request):
    try:
        user = User.objects.get(username = request.POST['username'])
    except:
        messages.error(request, "The username entered is not in our database, please try again!", extra_tags = "loginerror")
        return redirect(intro)

    password = request.POST['password']
    correctpw = user.password
    print password
    print correctpw

    if bcrypt.checkpw(password.encode(), correctpw.encode()):
        request.session['loggedIn'] = user.id
        return redirect(index)

    else:
        messages.error(request, "The password associated with that username was not provided", extra_tags = "loginerror")
        return redirect(intro)

def getcategory(request):
    category = request.POST['category']
    location = request.POST['location'].replace(" ","+")
    keyword = request.POST['keyword'].replace(" ", "+")
    # request.session['category'] = category
    # request.session['location'] = location
    print category
    print location
    #category = "movies_film"
    #url = "http://eventful.com/oauth/authorize?oauth_token=6ea35d914da91eec8c00"
    url = "http://api.eventful.com/json/events/search?app_key=29hhnm59QqVdfQWf&category=" +category+ "&location=" +location+ "&date=This Week&page_size=1000&keywords=" +keyword+""
    #url = "http://api.eventful.com/json/events/search?app_key=29hhnm59QqVdfQWf&date=ThisWeek&Location=Florida&page_size=50&"
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

def getpage(request):
    pass

def test(request):
    return render(request, 'bored_no_more_app/test.html')

def addEvent(request):
    try:
        address = request.POST['address']
    except:
        address = " "
    try:
        start = request.POST['start']
    except:
        start = " "
    
    try:
        stop = request.POST['stop']
    except:
        stop = " "
    
    try:
        description = request.POST['desc']
    except:
        description = " "
    
    name = request.POST['title']
    Event.objects.create(name = name, location = address, start = start, stop = stop, description = description, user = User.objects.get(id = request.session['loggedIn']) )
    # event = Event.objects.order_by('-id')[0]
    user = User.objects.get(id = request.session['loggedIn'])
    users = Event.objects.order_by('-id')[0].user.username
    events = user.events

    return redirect(index)

def userEvents(request):
    user = User.objects.get(id = request.session['loggedIn'])
    events = user.events.values()
    context = {
        'events':events,
        'user':user
    }

    return render(request, 'bored_no_more_app/userPage.html', context)

def deleteEvent(request, variable):
    Event.objects.get(id = variable).delete()

    return redirect(userEvents)

def logout(request):
    del request.session['loggedIn']
    return redirect(intro)









    