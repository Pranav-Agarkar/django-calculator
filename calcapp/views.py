from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse

# Create your views here.

# ---------------------------- Defined Variables ----------------
pi = 22/7
hero = 0
one = 1
two = 2
three = 3
four = 4
five = 5
six = 6
seven = 7
eight = 8
nine = 9

# ========================================================== common ==========================================================


def index(request):
    act = 'active'
    return render(request, 'index.html', {'active': act})


def contact(request):
    act = 'active'
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.save()
        return render(request, 'contact.html')
    return render(request, 'contact.html', {'activecontact': act})


# ========================================================== Periemeter =======================================

 ########## --- circle --- #########

def circle(request):
    active = 'active'
    return render(request, 'circleperi.html', {'activecircle': active})


def circleres(request):
    val1 = float(request.POST["radius"])
    res = two * pi * val1
    active = 'active'
    return render(request, 'circleperi.html', {'activecircle': active, 'result': res, 'radius': val1})

########## ----- Semi-Circle ---- ######


def semicircle(request):
    active = 'active'
    return render(request, 'semicircle.html', {'activesemi': active, })


def semicircleres(request):
    val1 = float(request.POST["radius"])
    res = pi*val1+two+val1
    active = 'active'
    return render(request, 'semicircle.html', {'ressemi': res, 'activesemi': active, 'val1semi': val1})

# ========================================================== Area ==============================================


# ========================================================== Volume =============================================


# ========================================================== Total Surface Area =================================


# ========================================================== Curve Surface Area =================================
