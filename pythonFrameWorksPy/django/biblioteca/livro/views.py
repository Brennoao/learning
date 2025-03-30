from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from usuarios.models import Usuario
from .models import Livros, Categoria, Emprestimos
from .forms import CadastroLivro, CategoriaLivro

def home(request):
    identificador = request.session['usuario']

    if identificador:
        usuario = Usuario.objects.get(id = identificador)

        livros = Livros.objects.filter(usuario = usuario)
        livros_emprestar = Livros.objects.filter(usuario = usuario).filter(emprestado = False)
        livros_total = livros.count()

        form = CadastroLivro()
        form.fields['usuario'].initial = identificador
        form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)

        form_categoria = CategoriaLivro()
        form_categoria.fields['usuario'].initial = identificador

        usuarios = Usuario.objects.all()

        return render(request, 'home.html', {'livros': livros, 'usuario_logado': identificador, 'form': form, 'form_categoria': form_categoria, 'usuarios': usuarios, 'livros_emprestar': livros_emprestar, 'livros_total': livros_total})
    else:
        return redirect('/auth/login/?status=2')

def ver_livros(request, id):
    identificador = request.session['usuario']
    identificado1 = request.session.get('usuario')

    if identificado1:
        livros = Livros.objects.get(id = id)

        if identificado1 == livros.usuario.id:
            categoria_livro = Categoria.objects.filter(usuario_id = identificador)
            emprestimos = Emprestimos.objects.filter(livro = livros)

            form_categoria = CategoriaLivro()
            usuarios = Usuario.objects.all()
            livros_emprestar = Livros.objects.filter(usuario = identificador).filter(emprestado = False)
            
            return render(request, 'ver_livro.html', {'livro': livros, 'categoria': categoria_livro, 'emprestimos': emprestimos, 'id_livro': id, 'livros_all': livros_emprestar, 'form_categoria': form_categoria, 'usuarios': usuarios})
        
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
        
def cadastrar_emprestimo(request):
    if request.method == 'POST':
        mome_emprestado = request.POST.get('mome_emprestado')
        mome_emprestado_anonimo = request.POST.get('mome_emprestado_anonimo')
        livro = request.POST.get('livro')

        if mome_emprestado_anonimo :
            emprestimo = Emprestimos(mome_emprestado_anonimo=mome_emprestado_anonimo, livro_id=livro)
        else:
            emprestimo = Emprestimos(mome_emprestado_id=mome_emprestado, livro_id=livro)
            print(mome_emprestado)

        emprestimo.save()

        livro = Livros.objects.get(id = livro)
        livro.emprestado = True
        livro.save()

        return redirect('/livro/home')
    
def devolver_livro(request, id):
    empretimo = get_object_or_404(Emprestimos, id=id)

    livro = empretimo.livro
    livro.emprestado = False
    livro.save()

    empretimo.data_devolucao = datetime.now()
    empretimo.save()

    return redirect(f'/livro/ver_livros/{livro.id}')