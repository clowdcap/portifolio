from django.shortcuts import render
from datetime import datetime
from .models import Post

# Create your views here.

def pagina_home(request):
    context = {
        "var": "Pagina Inicial",
    }
    return render(request, "pages/home.html", context)

def pagina_contato(request):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    context = {
        "horario": now,
        "horario2": current_time,
        "emailContent": "jose.marinho56@gmail.com",
        "telefoneContent": "(41) 99272-5388",
        "enderecoContent": "Rua tal, 250 - Sala 2 - Bairro X, Cidade-UF"
    }
    return render(request, "pages/contato.html", context)


def pagina_projetos(request):
    obj = Post.objects.all()
    
    context = {
        'projetos': obj,    
    }
    return render(request, "pages/projetos.html", context)