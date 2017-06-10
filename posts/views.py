from django.shortcuts import render


def index(request, page='index'):
    return render(request,'base.html')

def login(request, page='login'):
    return render(request,'login.html')

def logout(request, page='logout'):
    return render(request,'logout.html')

def singin(request, page='singin'):
    return render(request,'singin.html')