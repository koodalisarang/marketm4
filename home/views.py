import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from home.models import register, stokein, busket,order,amount

def home(request):
    try:
        request.session['orderid']=1000
        if request.session['member_id'] == "admin":
            return render(request,'admin.html')
        else:
           id=request.session['member_id']
           sto = stokein.objects.all()
           return render(request,'index.html',{'stoke':sto,'id':id})
    except:
        sto = stokein.objects.all()
        return render(request, 'index.html', {'stoke': sto})
def registers(request):
    return render(request,'register.html')
def registerdone(request):
    na=request.POST['username']
    em=request.POST['email']
    pa=request.POST['password']
    cp=request.POST['confirmpass']
    mo=request.POST['phone']
    ad=request.POST['address']
    if pa==cp:
        try:
            reg=register(username=na,email=em,password=pa,phone=mo,address=ad)
            reg.save()
            return login(request)
        except:
            return render(request, 'register.html', {'error': "please check once more!!!"})
    else:
        return render(request, 'register.html',{'error':"please check the password"})

def login(request):
    return render(request,'login.html')
def logindone(request):
    mo = request.POST['phone']
    pa = request.POST['password']
    try:
        if mo == "admin" and pa =="admin":
            request.session['member_id'] = "admin"
            return render(request, 'admin.html')
        else:
            det = register.objects.get(phone=mo)
            if det.password==pa:
                request.session['member_id']= det.phone
                return home(request)
            else:
                return render(request, 'login.html', {'error': "please check the password"})
    except:
        return render(request, 'login.html', {'error': "please check the password"})
def searchcategory(request):
    ca=request.POST['item']
    sto = stokein.objects.filter(category=ca)
    return render(request, 'index.html', {'stoke': sto})
def searchitem(request):
    try:
        it = request.POST['item']
        sto = stokein.objects.filter(itemname=it)
        if sto:
            return render(request, 'index.html', {'stoke': sto})
        else:
            return render(request, 'index.html',{'searcherror':'please search correctly'})

    except:
        print("work")
        return render(request, 'index.html', {'searcherror':'please search correctly'})
def addtobusket(request):

        id=request.POST['itemid']
        #qu=request.POST['quantity']
        print(id)
        #print(qu)
        det = stokein.objects.get(itemid=id)
        n=det.itemname
        p=det.price
        print(p)
        ph = request.session['member_id']
        #if det.type:
            #onegram=int(p)/1000
           # tp=onegram*int(qu)
        #else:
           # tp=int(qu)*int(p)
            #print(tp)
        bus=busket(phone=ph,itemid=id,itemname=n,price=p,total=0)
        bus.save()
        return home(request)

        return render(request, 'index.html', {'error1': "PLEASE LOG IN"})
def orderidset(request):
    print("orderid set workkkkkkkkkkkkkkkkkkkkkkkkkk upppppppppppppp")
    ord = request.session['orderid']
    if ( order.objects.filter(orderid=int(ord)).exists() ):
        print("orderid set workkkkkkkkkkkkkkkkkkkkkkkkkk")
        plus=int(ord)+1
        request.session['orderid']=plus
        return orderidset(request)
    else:
        print("error")
        return buy1(request)
def userlistview(request):
    ph = request.session['member_id']
    amo = amount.objects.filter(phone=ph)
    return render(request, 'userorderlist.html', {'amount': amo})
def viewbusket(request):
    try:
        ord = request.session['orderid']
        ph = request.session['member_id']
        #addr=register.objects.get(phone=ph)
        bus=busket.objects.filter(phone=ph)
        if bus:
            s = 0
            for i in bus:
                print(i.price)
                s = s + int(i.price)
            print("total=",s)
            print("s",bus)
            print("hereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
            return render(request,'busket.html',{'busket':bus,'grandtotal':s})
        else:
            return render(request,'index.html',{'error1':"NOTING TO SHOW"})
    except:
        return render(request, 'index.html', {'error1':"PLEASE LOG IN"})
def deletecart(request):
    name = request.POST['itemid']
    dele=busket.objects.get(itemid=name)
    dele.delete()
    print(name)
    print("deleteeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
    return viewbusket(request)
def buy1(request):
        orde = request.session['orderid']
        ph = request.session['member_id']
        da=datetime.date.today()
        pa = int(request.POST['pay'])
        bus = busket.objects.filter(phone=ph)
        print("hai")
        for i in bus:
            ord = order(orderid=int(orde), phone=ph, itemid=i.itemid , itemname=i.itemname  , price=i.price , total=i.total, date=da)
            ord.save()
        print("ok")
        dele = busket.objects.filter(phone=ph)
        dele.delete()
        amo=amount(orderid=orde,phone=ph,date=da,price=pa)
        amo.save()
        print("yes")
        return userlistview(request)
def myorder(request):
    try:
        ph = request.session['member_id']
        ordid=request.POST['orderidi']
        print(ordid)
        addr=register.objects.get(phone=ph)
        bus = order.objects.filter(orderid=int(ordid))
        am=amount.objects.get(orderid=int(ordid))
        amo=am.price
        if bus:
            print("hereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
            return render(request, 'myorder.html', {'busket': bus,'address':addr, 'grandtotal': amo,'amo':am})
        else:
            return render(request, 'index.html', {'error1': "NOTING TO SHOW"})
    except:
        return render(request, 'index.html', {'error1': "NOTING TO SHOW"})

def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        return HttpResponse("error occurred")
    return home(request)
def orderreceive(request):

    ph=request.POST['ordid']
    amo=amount.objects.get(orderid=int(ph))
    if amo.status==True:
        delee = amount.objects.filter(orderid=int(ph))
        dele = order.objects.filter(orderid=int(ph))
        delee.delete()
        dele.delete()
        return home(request)
    else:
        return userlistview(request)
# ADMIN
def adminhome(request):
    return render(request,'admin.html')
def update(request):
    sto = stokein.objects.all()
    return render(request, 'indexupdate.html', {'stoke': sto})
def orders(request):
    amo=amount.objects.all()
    return render(request,'orderlist.html',{'amount':amo})
def updateit(request):
    it=request.POST['itemid']
    na=request.POST['itemname']
    pr=request.POST['price']
    stokein.objects.filter(itemid=it).update(itemname=na,price=pr)
    return update(request)
def searchitemadmin(request):
        it = request.POST['itemid']
        print(it)
        sto = stokein.objects.filter(itemid=it)
        if sto:
            return render(request, 'indexupdate.html', {'stoke': sto})
        else:
            return render(request, 'indexupdate.html',{'searcherror': 'please search correctly'})

def searchcategoryadmin(request):
    ca = request.POST['item']
    sto = stokein.objects.filter(category=ca)
    return render(request, 'indexupdate.html', {'stoke': sto})
def ordershow(request):
    ph=request.POST['ordid']
    ord = order.objects.filter(orderid=int(ph))
    am = amount.objects.get(orderid=int(ph))
    mob=am.phone
    addr = register.objects.get(phone=mob)
    amo = am.price
    return render(request, 'ordershow.html', {'order':ord,'address':addr, 'grandtotal': amo,'ordid':am})
def ordersend(request):
    ph=request.POST['orderid']
    amount.objects.filter(orderid=ph).update(status=True)
    return orders( request)
