from django.shortcuts import render

def index(request):
    context = {}
    html = 'index.html'
    return render(request, html, context)

def home(request):
    context = {}
    html = 'home.html'
    return render(request, html, context)

def dashboard(request):
    context = {}
    html = 'home.html'
    return render(request, html, context)

def products(request):
    context = {}
    html = 'home.html'
    return render(request, html, context)

def users(request):
    context = {}
    html = 'home.html'
    return render(request, html, context)

def all_users(request):
    context = {}
    html = 'home.html'
    return render(request, html, context)

def add_user(request):
    context = {}
    html = 'home.html'
    return render(request, html, context)

def add_user_single(request):
    context = {}
    html = 'home.html'
    return render(request, html, context)

def add_user_file(request):
    context = {}
    html = 'home.html'
    return render(request, html, context)

def other_menu(request):
    context = {}
    html = 'home.html'
    return render(request, html, context)