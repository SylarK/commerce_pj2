from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from auctions.models import *


def index(request):

    list_view = Auction.objects.all()

    return render(request, "auctions/index.html", {
        'list_view':list_view
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def newauction(request):
    if request.method == 'POST':

        title = request.POST['title']
        desc = request.POST['description']
        detail = request.POST['detail']
        init = request.POST['value']
        url = request.POST['url']
        cat = request.POST['categorie']

        new = Auction(user=request.user, title=title, description=desc, detail=detail, init=init, url=url, cat=cat)
        new.save()
        
        return redirect('index')

    else:

        return render(request, 'auctions/new_auction.html')

def view_auction(request, item_title):

    auction_view = Auction.objects.get(title=item_title)
    watchlist = WatchList.objects.filter(user=request.user, toauction=auction_view)
    msg = ''

    if request.method == 'POST':

        if request.POST['type-form'] == 'comment':
            text = request.POST['comment']
            new_comment = Comment(user=request.user, toauction=auction_view, text=text)
            new_comment.save()
            
        else:
            bid = request.POST['newbid']
            #check
            if check(bid, auction_view.init):
                newbid = Bid(user=request.user, toauction=auction_view, value=bid)
                auction_view.init = bid
                auction_view.save()
                newbid.save()
            else:
                msg = 'Your bid must be greater than a current bid.'
                                       
    comments = Comment.objects.filter(toauction=auction_view)
    return render(request, 'auctions/view.html', {
        'auction':auction_view,
        'comments':comments,
        'msg':msg,
        'watchlist':watchlist
        })

def check(value1, value2):
    return int(value1) > int(value2)

def man_watchlist(request, item_title):

    auction_view = Auction.objects.get(title=item_title)

 
    try:
        watch = WatchList.objects.get(user=request.user, toauction=auction_view).delete()

    except:
        watch = WatchList(user=request.user, toauction=auction_view)
        watch.save()

    return redirect('view', item_title=item_title)
