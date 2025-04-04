from django.shortcuts import redirect, render

from restaurante.models import Categoria, Produto

# Create your views here.
def produtos(request):
    categorias = Categoria.objects.all()
    categoria_filtro = request.GET.get('categoria')
    if categoria_filtro:
        produtos = Produto.objects.filter(categoria__id=categoria_filtro)
    else:
        produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos, 'categorias': categorias})

def cadastrar_produto(request):
    categorias = Categoria.objects.all()
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        return render(request, 'cadastrar_produto.html', {'categorias': categorias})
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        descricao = request.POST.get('descricao')
        categoria_id = request.POST.get('categoria')

        categoria = Categoria.objects.get(id=categoria_id)

        produto = Produto(nome=nome, preco=preco, descricao=descricao, categoria=categoria)
        produto.save()
        return redirect(request, 'produtos')

