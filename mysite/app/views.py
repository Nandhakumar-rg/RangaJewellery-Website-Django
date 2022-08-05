from cgitb import html
from datetime import datetime
from statistics import quantiles
import time
import datetime
from distutils import errors
from distutils.log import error
import re
from tkinter import Variable
from unicodedata import name
from urllib import request
from xml.etree.ElementTree import tostring
from django.template import loader
from django import template
from datetime import timedelta 

from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import Template,Context

from app.models import sign, move, jewel, Itemcart, adminsite, orders
from django.contrib.auth import authenticate, login, logout
from django.contrib import sessions
from json import dumps

from django.conf import settings # new
from django.views.generic.base import TemplateView
import stripe
# Create your views here.

def home(request):
    desti = []
    curname = "default"
    desti = move.objects.all()
    if request.session.get('username'):
        try :
            curname  = (','.join(request.session['username']))
            img = sign.objects.get(uname = curname)
            return render(request, 'home.html', {
        'desti': desti,
        'img' : img.profile_pic
        })
        except:
            pass
 
   
    print("ok")
    return render(request, 'home.html', {
        'desti': desti,
        })
   

def signup(request):
    
    if request.method == "POST":
        fname = request.POST['fname']
        email = request.POST['email']
        uname = request.POST['uname']
        password = request.POST['password']
        print(fname,email,uname,password)
        ins = sign(fname=fname,email=email,uname=uname,password=password)
        ins.save()
        print("Data saved successfully")
    return render(request,'signup.html')



def logout(request):
    if request.session.get('username'):
      del request.session['username']
    request.session.modified = True
    return HttpResponseRedirect('/login/')
def moves(request):
    if request.method == "POST":
        url = request.POST['url']
        print(url)
        ins = move(url=url)
        ins.save()
        print("Data saved successfully")
    return render(request,'homebackground.html')

def jeweladd(request):
    if request.method == 'POST':
        jname = request.POST['jname']
        url = request.POST['url']
        price = request.POST['price']
        ins = jewel(jname=jname,url=url,price=price)
        ins.save()
        print("Data saved successfully")
    return render(request,'jewelsa.html')

def jewels(request):
    return render(request,'jewels.html')


def login(request):
    error = False
    if request.method == "POST":
        boole = False
        uname = request.POST['uname']
        password = request.POST['password']
        for each in sign.objects.all():
            if(each.uname == uname and each.password == password):
               
                request.session['username'] = [uname]
                print(request.session.get('username'))
                request.session.modified = True
                return HttpResponseRedirect('/home',{
                    #    error:
                })
            else:
                # errors.append('error')
                error=True
               
        for each in adminsite.objects.all():
            if(each.uname == uname and each.password == password):
               
                request.session['username'] = [uname]
                print(request.session.get('username'))
                request.session.modified = True
                return HttpResponseRedirect('/admincontrol',{
                    #    error:
                })
            else:
                error=True       
    return render(request,'login.html',{
        'ename' : "Invalid username or password ",
        'error':error
    })




def update(request):
    print("the method is",request.method)
    errors = False
    if(request.method == "POST"):
        print("Data updated successfully!")
        name=request.POST['uname']
        mail=request.POST['email']
        npassword=request.POST['npassword']
        sign.objects.filter(uname=name,email=mail).update(password=npassword)
        print("Data updated successfully!")
    else:
        errors=True
        print("No data found")

        
    return render(request,'update.html',{
        'ename' : "No data found ",
        'errors':errors
    })

def delete(request):
    if request.method == "POST":
        jname=request.POST['jname']
        dele=jewel.objects.get(jname=jname)
        dele.delete()
        print("Data deleted successfully")
    else:
        print("Redirected")
    return render(request,'jewelsd.html')

def profile(request):
    active_user = request.session['username'][0]
    if request.method == "POST":
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        dOB = request.POST.get('dob')
        email= request.POST.get('email')
        profile = request.POST.get('url')
        if profile == '':
            sign.objects.filter(uname=active_user).update(dob=dOB, gender=gender, address=address, email=email)
        else:
            sign.objects.filter(uname=active_user).update(dob=dOB, gender=gender, address=address, email=email, profile_pic=profile)
        return HttpResponseRedirect('/profile')
    return render(request,'profile.html',{
        'account_info': sign.objects.filter(uname=active_user)[0],
    })
def index(request):
    return render(request,'index.html')

def bangle(request):
    count = 0
    for each in jewel.objects.all():
        if each.jname == "bangle":
            count = count+1
    data = {}
    i=0
    
    
    for each in jewel.objects.all():
        if each.jname == "bangle":
            data[i] = ([each.jname,each.url,each.price])
            i=i+1

    dataJSON =dumps(data) 
    return{
        'bang':dataJSON
    }

def cart(request):
    return render(request,'cart.html')

def datacart(request):
    if request.method == 'GET':
        dc_id = request.GET['p_id']
        obj = jewel.objects.get(id=dc_id)
        jname = obj.jname
        jurl = obj.url
        jprice = obj.price
        try:
            CurrentUser = request.session['username'][0]
        except:
            pass
        d = Itemcart(icname=jname,icurl=jurl,icprice=jprice, uname=CurrentUser)
        d.save()
        return HttpResponse("Success!")
    else:
        return HttpResponse("Request method is not GET") 

def contact(request):
    return render(request,'contact.html')

def product(request):
    if request.method == 'POST':
        p_id = -1
        try: p_id= int(request.POST['p_id'])
        except: pass 
        request.session['Viewproduct'] = p_id
        request.session.modified = True
        print(request.session.get('Viewproduct'))
        return HttpResponse("Success")
    return render(request,'product.html')

def updateCart(request):
    if request.method == 'GET':
        id = request.GET['cart_id']
        newQuantity = int(request.GET['quantity'])
        Icrecord = Itemcart.objects.get(id=id)
        Jewelrecord = jewel.objects.get(url = Icrecord.icurl)
        ActualPrice = int(Jewelrecord.price)
        print(ActualPrice)
        Itemcart.objects.filter(id=id).update(quantity = newQuantity, icprice = ActualPrice*newQuantity)
    return HttpResponse("Success!")

# def payment(request):
#     return render(request,'payment.html')



stripe.api_key = settings.STRIPE_SECRET_KEY

class HomePageView(TemplateView):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


def charge(request): # new
    
    if request.method == 'POST':
        CheckoutData = Itemcart.objects.filter(uname = request.session['username'][0])
        amount = 0
        desc = " payment for :"
        for each in CheckoutData:
            amount = amount + int(each.icprice)
            desc = desc +' '+ each.icname + ', '
        desc = desc + ' is done successful for : '+ request.session['username'][0] + ' at ' + time.strftime("%H:%M:%S", time.localtime())
        charge = stripe.Charge.create(
            amount=amount*100,
            currency='inr',
            description=desc,
            source=request.POST['stripeToken']
        )
        Itemcart.objects.filter(uname = request.session['username'][0]).delete()
        ShippingAddress = sign.objects.filter(uname= request.session['username'][0])
        for each in CheckoutData:
            ins = orders(ocname= each.icname, ocurl= each.icurl, ocprice= each.icprice, quantity= each.quantity, uname= each.uname, address= ShippingAddress[0].address) 
            ins.save()
        return render(request, 'cart.html',{
            'message' : '<script>window.alert("Order Placed");</script>'
        })
def deleteCart(request):
    if request.method == "GET":
        cart_id = request.GET['cart_id']
        Itemcart.objects.filter(id=cart_id).delete()
        return HttpResponse("Success")


def collections(request):
    return render(request,'collections.html')

def about(request):
    return render(request,'about.html')



# admin pages
def admincontrol(request):
    return render(request,'admincontroll.html')
def adminUsers(request):
    return render(request,'adminUsers.html')
def deleteJewels(request):
    return render(request, 'deleteJewels.html')
def adminDelete(request):
    jewel_id = request.GET['jewel_id']
    jewel.objects.filter(id = jewel_id).delete()
    return HttpResponse("Success")



def orderHistory(request):
    return render(request, 'orderHistory.html')
def allOrders(request):
    return render(request, 'allOrders.html')
 