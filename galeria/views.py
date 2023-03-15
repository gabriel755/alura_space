from django.shortcuts import render


def index(req):
    data = {
        1: {"nome": "Nebulosa de Carina",
            "legenda": "webbtelescope.org/ NASA/ James Webb"},
        2: {"nome": "Galáxia NGC 1079", 
            "legenda": "nasa.org / NASA / Hubble"},
    }

    return render(req, 'galeria/index.html', {"cards": data})

def imagem(req):
    return render(req, 'galeria/imagem.html')