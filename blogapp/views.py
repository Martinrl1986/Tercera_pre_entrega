from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from boostrap_blog.forms import UserRegisterForm, SearchForm, ArticleForm
from blogapp.models import PortfolioItem, Article
from django.contrib.auth import login, authenticate, logout
from django.views.generic import DeleteView
from django import forms



def base(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            url_exitosa = reverse('base')
            return redirect(url_exitosa)
    else:
        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name='base.html',
        context={'form': formulario},
    )

def search(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = PortfolioItem.objects.filter(caption__icontains=query)

    search_form = SearchForm()

    return render(request, 'search.html', {'results': results, 'search_form': search_form})

def portfolio(request):
    portfolio_items = PortfolioItem.objects.all()
    return render(request, 'portfolio.html', {'portfolio_items': portfolio_items})

def about(request):
    return render(request, 'about.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirige a la página de inicio o a cualquier otra página deseada
            return redirect('base')
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
    
def logout_view(request):
    logout(request)
    return redirect('base')
    
def articles(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})

def article_list(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'article_list.html', context)
    
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles')
    else:
        form = ArticleForm()
    
    articles = Article.objects.all()
    context = {
        'form': form,
        'articles': articles
    }
    return render(request, 'create_article.html', context)

def article_delete(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        article.delete()
        return redirect('articles')
    
    context = {
        'article': article
    }
    return render(request, 'article_delete.html', context)

def article_confirm_delete(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        article.delete()
        return redirect('articles')
    return render(request, 'article_confirm_delete.html', {'article': article})


def article_edit(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles')
    else:
        form = ArticleForm(instance=article)
    
    context = {
        'form': form,
        'article': article
    }
    return render(request, 'article_edit.html', context)
class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('articles')
    template_name = 'article_confirm_delete.html'
    
    