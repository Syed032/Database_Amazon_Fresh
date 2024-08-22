from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def insert_data(request):
    return render(request, "home.html")

def login(request):
     return render(request, "index.html")

def saved(request):
    if request.method == "POST":
        data  = request.POST
        pname = data.get("Pname")
        Manu = data.get("Manu")
        Exp = data.get("Exp")
        Cname = data.get("Cname")
        Pnumber = data.get("Pnumber")
        Caddress = data.get("Caddress")
        Oname = data.get("Oname")
        Odate = data.get("Odate")
        Paymode = data.get("Paymode")
        Amt = data.get("Amt")
        # Oprice = data.get("Oprice")
        Qty = data.get("Qty")

        print(Cname)

        m1 = Products(product_name = pname, date_of_mnf = Manu, date_of_exp = Exp)
        m2 = Customer(customer_name=Cname, phone_number = Pnumber, address = Caddress)
        m3 = Orders(order_name = Oname, order_date = Odate)
        m4 = Payment(Payment_mode = Paymode, amount = Amt, )
        m5 = Order_details(order_quantity = Qty)

        m1.save()
        m2.save()
        m3.save()
        m4.save()
        m5.save()
    return render(request, "saved.html")

def display(request):
    m1 = Products.objects.all()
    m2 = Customer.objects.all()
    m3 = Orders.objects.all()
    m4 = Payment.objects.all()
    m5 = Order_details.objects.all()

    result = {
        'products' : m1,
        'customer' : m2,
        'orders' : m3,
        'payment' : m4,
        'orderdetails' : m5,
    }
    context = {'result': result}

    return render(request, "display.html", context)

def update(request, id):
    if request.method == "POST":
        data = request.POST
        pname = data.get("Pname")
        Manu = data.get("Manu")
        Exp = data.get("Exp")
        Cname = data.get("Cname")
        Pnumber = data.get("Pnumber")
        Caddress = data.get("Caddress")
        Oname = data.get("Oname")
        Odate = data.get("Odate")
        Paymode = data.get("Paymode")
        Amt = data.get("Amt")
        # Oprice = data.get("Oprice")
        Qty = data.get("Qty")

        m1 = Products.objects.get(id = id)
        m2 = Customer.objects.get(id = id)
        m3 = Orders.objects.get(id = id)
        m4 = Payment.objects.get(id = id)
        m5 = Order_details.objects.get(id = id)

        m1.product_name = pname
        m1.date_of_mnf = Manu
        m1.date_of_exp = Exp
        m1.save()

        m2.customer_name = Cname
        m2.phone_number = Pnumber
        m2.address = Caddress
        m2.save()

        m3.order_name = Oname
        m3.order_date = Odate
        m3.save()

        m4.Payment_mode = Paymode
        m4.amount = Amt
        m4.save()

        m5.order_quantity = Qty
        m5.save()

        return redirect("/display")
    print(id)
    m3 = Products.objects.get(id = id)
    ref = m3.id
    context = {"m3" : ref}
    return render(request, "update.html", context)

def delete_data(request, id):
        m1 = Products.objects.get(id = id)
        m2 = Customer.objects.get(id = id)
        m3 = Orders.objects.get(id = id)
        m4 = Payment.objects.get(id = id)
        m5 = Order_details.objects.get(id = id)

        m1.delete()
        m2.delete()
        m3.delete()
        m4.delete()
        m5.delete()
        return redirect("/display")