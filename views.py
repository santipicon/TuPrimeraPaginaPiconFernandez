from django.shortcuts import render, redirect
from .forms import AutorForm, CategoriaForm, PostForm
from .models import Post, Autor

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')  # Redirige a la lista de autores o donde prefieras
    else:
        form = AutorForm()
    return render(request, 'crear_autor.html', {'form': form})
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = CategoriaForm()
    return render(request, 'blog/crear_categoria.html', {'form': form})

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_posts')  # Redirige a la lista de posts o a donde prefieras
    else:
        form = PostForm()
    return render(request, 'crear_post.html', {'form': form})
def buscar_post(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        resultados = Post.objects.filter(titulo__icontains=query) if query else None
        return render(request, 'blog/buscar_post.html', {'resultados': resultados, 'query': query})

def lista_posts(request):
    posts = Post.objects.all().order_by('-fecha_creacion')
    return render(request, 'lista_posts.html', {'posts': posts})

def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'lista_autores.html', {'autores': autores})