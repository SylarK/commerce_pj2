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
                auction_view.winner = request.user
                auction_view.save()

            else:
                msg = 'Your bid must be greater than a current bid.'

    #if user is not logged
    try: 
        watchlist = WatchList.objects.filter(user=request.user, toauction=auction_view)
    except:
        watchlist = False
            
                                       
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

def view_watchlist(request):

    watch = WatchList.objects.filter(user=request.user)

    return render(request, 'auctions/watchlist.html', {
        'watchlist':watch
    })

def close(request, item_title):

    auction_view = Auction.objects.get(title=item_title)
    
    #changing the status of the auction
    alt = auction_view
    alt.status = 0
    alt.save()

    #changing the alert status of the winner
    winner = User.objects.get(username=auction_view.winner.username)
    winner.alert = 1
    winner.save()

    #save result into AuctionResult
    result = ResultAuction(user=winner, toauction=auction_view)
    result.save()

    return redirect('index')

def return_home(request, item_title):

    auction_view = Auction.objects.get(title=item_title)
    watch = WatchList.objects.get(user=request.user, toauction=auction_view).delete()

    return redirect('index')

def result(request):

    if request.user.alert == 1:
        request.user.alert = 0
        request.user.save()

    results = ResultAuction.objects.filter(user=request.user)

    return render(request, 'auctions/result.html',{
        'results':results
    })

def filtered(request, categorie):

    list_filtered = Auction.objects.filter(cat=categorie)

    return render(request, 'auctions/filter.html', {
        'list_filtered':list_filtered
    })