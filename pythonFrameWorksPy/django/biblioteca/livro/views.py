from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Livros, Categoria, Emprestimos

# Create your views here.

def home(request):
    if request.session.get('usuario'):
        identificador = request.session['usuario']
        usuario = Usuario.objects.get(id = identificador)

        livros = Livros.objects.filter(usuario = usuario)
        return render(request, 'home.html', {'livros': livros})
    else:
        return redirect('/auth/login/?status=2')

def ver_livros(request, id):
    identificador = request.session['usuario']
    if request.session.get('usuario'):
        livros = Livros.objects.get(id = id)
        if request.session.get('usuario') == livros.usuario.id:
            categoria_livro = Categoria.objects.filter(usuario_id = identificador)
            emprestimos = Emprestimos.objects.filter(livro = livros)
            return render(request, 'ver_livro.html', {'livro': livros, 'categoria': categoria_livro, 'emprestimos': emprestimos})
        else:
            return HttpResponse('livro não existe')
    return redirect('/auth/login/?status=2')