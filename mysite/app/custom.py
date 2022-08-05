import re
from app.models import sign , jewel ,Itemcart, orders
from json import dumps


def isLogged(request):
    isThere = request.session.get('username')
    if isThere == None:
        isThere = 0
    else:
        isThere = 1
    return {
        'isLogged' : isThere
    }
def status(request):
    if request.session.get('username'):
        try :
            curname  = (','.join(request.session['username']))
            img = sign.objects.get(uname = curname)
            return {
        'img' : img.profile_pic,
        'status' : True,
        }
        except:
            pass
    return({
            'status' : False
        })
def banglepass(request):
    l = []
    l = jewel.objects.filter(jname="bangle")
    return {
        'bangle' : l,
    }

def chainpass(request):
    l = []
    l = jewel.objects.filter(jname="chain")
    return {
        'chain' : l,
    }

def ringpass(request):
    l = []
    l = jewel.objects.filter(jname="Ring")
    return {
        'ring' : l,
    }

def sringpass(request):
    l = []
    l = jewel.objects.filter(jname="Silver ring")
    return {
        'sring' : l,
    }

def ankletspass(request):
    l = []
    l = jewel.objects.filter(jname="Silver anklets")
    return {
        'anklets' : l,
    }

def schainpass(request):
    l = []
    l = jewel.objects.filter(jname="Silver chain")
    return {
        'schain' : l,
    }

def braceltspass(request):
    l = []
    l = jewel.objects.filter(jname="Platinum bracelets")
    return {
        'bracelts' : l,
    }

def pchainpass(request):
    l = []
    l = jewel.objects.filter(jname="Platinum chain")
    return {
        'pchain' : l,
    }

def pringpass(request):
    l = []
    l = jewel.objects.filter(jname="Platinum rings")
    return {
        'pring' : l,
    }

def dbraceltspass(request):
    l = []
    l = jewel.objects.filter(jname="Diamond bracelets")
    return {
        'dbracelts' : l,
    }

def dchainpass(request):
    l = []
    l = jewel.objects.filter(jname="Diamond chain")
    return {
        'dchain' : l,
    }

def dringpass(request):
    l = []
    l = jewel.objects.filter(jname="Diamond rings")
    return {
        'dring' : l,
    }

def eringpass(request):
    l = []
    l = jewel.objects.filter(jname="Ear ring")
    return {
        'ering' : l,
    }

def allpass(request):
    l = []
    l = jewel.objects.all()
    return {
        'all' : l,
    }

def cartdata(request):
    data = []
    try:
        data = Itemcart.objects.filter(uname=request.session['username'][0])
    except:
        pass
    return{
        'cartdata' : data,
        'isNoItem' : len(data)
    }

def adminUsers(request):
    return {
        'users' : sign.objects.all()
    }

def CheckoutBill(request):
    CurrentUser = ""
    try:
        CurrentUser = request.session['username'][0]
    except:
        pass
    CheckOutPrice = 0
    try:
        for each in Itemcart.objects.all():
            CheckOutPrice = CheckOutPrice + int(each.icprice)
    except:
        print("Error! no cart data found for current user")
    return {
    'CheckoutBill' :  (CheckOutPrice/80)*100,
    'CurrentUser' : CurrentUser
    }

def orderdata(request):
    CurrentUser = ""
    try:
        CurrentUser = request.session['username'][0]
    except:
        pass
    data = orders.objects.filter(uname = CurrentUser)
    return {
        'orderdata' : data,
        'isNoOrder' : len(data),
    }

def allorderdata(request):
    data = {}
    orderUserdata = []
    for each in orders.objects.all():
        record = sign.objects.filter(uname= each.uname)
        data =  {
            'id' : each.id,
            'user_pic' : record[0].profile_pic
        }
        orderUserdata.append(data)
    return {
        'allorderdata' : orders.objects.all(),
        'allorderUserdata':orderUserdata, 
        'isTotalOrders' : len(orders.objects.all())
    }

def ViewProduct(request):
    p_id = request.session.get('Viewproduct')
    print("custom page ",request.session.get('Viewproduct'))
    record = jewel.objects.filter(id= p_id)
    try:print(record)
    except:pass
    return {
        'CurrentProduct' : record
    } 
