from django.shortcuts import render, redirect
from .models import Post, Autor, Account
from .forms import PostForm, AutorForm
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html')

def about_me(request):
    return render(request, 'about-me.html')

def about_website(request):
    return render(request, 'about-website.html')

def projects(request):
    return render(request, 'projects.html')

def web_programming(request):
    return render(request, 'web-programming.html')

def contact(request):
    return render(request, 'contact.html')

def javascript(request):
    return render(request, 'javascript.html')

def blog_posts(request):
    posts = Post.objects.all()
    form = PostForm()
    account = Account.objects.first()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_posts')

    context = {'posts': posts, 'form': form, 'account': account}
    return render(request, 'blog.html', context)

def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.likes += 1
    post.save()
    return redirect('blog_posts')

def editar_post(request, post_id):
    post = Post.objects.get(id=post_id)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_posts')

    context = {'form': form}
    return render(request, 'editar_post.html', context)

def apagar_post(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('blog_posts')

    context = {'post': post}
    return render(request, 'apagar_post.html', context)

def adicionar_autor(request):
    form = AutorForm()

    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_posts')

    context = {'form': form}
    return render(request, 'adicionar_autor.html', context)