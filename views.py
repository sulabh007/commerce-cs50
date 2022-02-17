from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.db.models.fields import NOT_PROVIDED
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Bid, Category, User, Listing, Comment, WatchList


def index(request):
    
    return render(request, "auctions/index.html"
    )


def list_of_item(request):
    listing=Listing.objects.all()
    return render(request, "auctions/listing.html",{
        "listings":listing
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


def listing(request, listing_id):
    
        
    listing=Listing.objects.get(pk=listing_id)
    comment=Comment.objects.filter(title=listing_id)
    wishl=WatchList.objects.filter(item=listing).first()
    bidding= Bid.objects.filter(title=listing).first()
    return render(request, "auctions/item.html", {
        "item":listing,
        "comments":comment,
        "buyer":request.user.username,
        "check":wishl,
        "highest_bid":bidding
        })


@login_required
def create_listing(request):
    
    Cat=Category.objects.all()
    if request.method== "POST":
        
        item=Listing()
        item.user=request.user.username
        item.title=request.POST.get('title')
        item.description=request.POST.get('description')
        item.price=request.POST.get('price')
        
        item.image_url=request.POST.get('image_url')
        item.category=request.POST.get('category')
        item.save()
        return render(request, "auctions/index.html")
    else:
        return render(request, "auctions/create.html",{
            "seller":request.user.username,
            "category":Cat
        })
        
        
def category(request):
    if request.method== "POST":
        form= Category()
        if request.method=="POST":
            form.cat=request.POST.get('category')
            form.save()
            return HttpResponseRedirect(reverse("category"))
        else:
            cat=Category.objects.all()
            return render(request, "auctions/category.html",{
                "form": form,
                "categories":cat
            })
    cat=Category.objects.all()
    form= Category()
    return render(request, "auctions/category.html", {
        "form": form,
        "categories":cat})

def show_category(request, category_id):
    cate=Category.objects.get(pk=category_id)
    listing=Listing.objects.filter(category=cate)
    return render(request, "auctions/cate.html",{
        "listings":listing
    })

def add_comm(request, listing_id):
    
    
    if request.method =="POST":   
        comm_form=Comment()
        comm_form.user=request.user.username 
        comm_form.title=Listing.objects.get(pk=listing_id) 
        comm_form.comment=request.POST.get('Comment')
        comm_form.save()
        return redirect(index)
    else:
        return render(request, "auctions/addcomm.html",{
            "item":Listing.objects.get(pk=listing_id),
            "item_id":listing_id
        })
        

def watch_list(request):
    userid=request.user
    watching=WatchList.objects.filter(name=userid)
    return render(request, "auctions/wishlist.html",{
        "listings":watching
        })

def wish(request, listing_id):
    wish=WatchList.objects.get(pk=listing_id)
    item=Listing.objects.get(title=wish.item)
    return redirect('item', item.id)

def add_wish(request, listing_id):
    addwish=WatchList()
    addwish.name=request.user
    addwish.item=Listing.objects.get(pk=listing_id) 
    addwish.save()
    return redirect(watch_list)


def remove_wish(request, listing_id):
    item=Listing.objects.get(pk=listing_id)
    wish=WatchList.objects.get(item=item)
    wish.delete()
    return redirect(watch_list) 


def bid(request, listing_id):
    if request.method=="POST":   
        item=Listing.objects.get(pk=listing_id)
        bidding=int(request.POST.get('Price'))
        if item.current_bid==None:
            if bidding >=item.price:
                add_bid=Bid()
                add_bid.user=request.user.username
                add_bid.title=Listing.objects.get(pk=listing_id)
                add_bid.price=bidding
                item.current_bid=add_bid.price
                item.save()
                add_bid.save()
                return redirect(index)
        elif bidding >item.current_bid:
            add_bid=Bid.objects.get(title=item)
            add_bid.user=request.user.username
            add_bid.price=bidding
            item.current_bid=add_bid.price
            item.save()
            add_bid.save()
            return redirect(index)
            
        else:
            return render(request, "auctions/bid_error.html", {
                "message": f"Error: Your bid for item '{item}' is too low. Bid more than the current value."
                })

    else:
        return render(request, "auctions/addbid.html",{
            "item":Listing.objects.get(pk=listing_id),
            "item_id":listing_id
        })
    

def sell(request, listing_id):
    item=Listing.objects.get(pk=listing_id)
    item.sold=True
    item.save()
    return redirect('item', item.id)