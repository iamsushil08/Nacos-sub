from django.shortcuts import render ,redirect


def home(request):
    return render(request,'core/home.html')

def shop(request):
    return render(request,'core/shop.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

