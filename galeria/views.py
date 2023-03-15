from django.shortcuts import render

def index(req):
    return render(req, 'galeria/index.html')

def imagem(req):
    return render(req, 'galeria/imagem.html')