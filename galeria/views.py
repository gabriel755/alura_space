from django.shortcuts import render

def index(req):
    return render(req, 'galeria/index.html')