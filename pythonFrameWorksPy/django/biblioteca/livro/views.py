from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Livros, Categoria, Emprestimos
from .forms import CadastroLivro, CategoriaLivro

def home(request):
    identificador = request.session['usuario']

    if identificador:
        usuario = Usuario.objects.get(id = identificador)
        livros = Livros.objects.filter(usuario = usuario)

        form = CadastroLivro()
        form.fields['usuario'].initial = identificador
        form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)
        form_categoria = CategoriaLivro()
        form_categoria.fields['usuario'].initial = identificador

        return render(request, 'home.html', {'livros': livros, 'usuario_logado': identificador, 'form': form, 'form_categoria': form_categoria})
    else:
        return redirect('/auth/login/?status=2')

def ver_livros(request, id):
    identificador = request.session['usuario']
    if request.session.get('usuario'):
        livros = Livros.objects.get(id = id)

        if request.session.get('usuario') == livros.usuario.id:
            categoria_livro = Categoria.objects.filter(usuario_id = identificador)
            emprestimos = Emprestimos.objects.filter(livro = livros)
            return render(request, 'ver_livro.html', {'livro': livros, 'categoria': categoria_livro, 'emprestimos': emprestimos, 'id_livro': id})
        
        else:
            return HttpResponse('livro não existe')
    return redirect('/auth/login/?status=2')

def cadastrar_livro(request):
    if request.method == 'POST':
        form = CadastroLivro(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/livro/home/')
        else:
            return HttpResponse('Formulário inválido')
        
def excluir_livro(request, id):
    # identificador = request.session['usuario']

    livro = Livros.objects.get(id = id).delete()
    return redirect('/livro/home')
 
def cadastrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaLivro(request.POST)
        verify = request.POST.get('usuario')

        if form.is_valid():
            if verify:
                form.save()
                return redirect('/livro/home')
        else:
            return HttpResponse('Formulário inválido')