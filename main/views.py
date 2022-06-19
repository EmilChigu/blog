from ast import IsNot
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Article, User, Comment
from django.db.models import Q, F
from.forms import ArticleForm




# Create your views here.

def loginPage(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('articles')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        

        try:
            user = User.objects.get(username = username)
            
        except:
            messages.error(request, 'The email or password is incorrect.')
        
        
        user = authenticate(request, username = username, password = password)
        

        if user is not None:
            login(request, user)
            return redirect('articles')
        else:
           messages.error(request, 'The email or password is incorrect, please try again.') 

    context = {'page':page}
    return render(request, 'main/register_login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')


def registerUser(request):
    page = 'register'

    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)

            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
           messages.error(request, 'Registration failed.')   

    context={'page':page, 'form':form}

    return render(request, 'main/register_login.html', context)

def home(request):
  

    # FETCH ARTICLES
    newest = Article.objects.all().order_by('-date_created')[:5]

    # Latest 4 with out featured
    articles = newest[1:]

    # FETCH LATEST ARTICLE
    featured = newest[0]

    

  

    context= {'articles': articles, 'featured': featured }
    # messages.info(request, 'Three credits remain in your account.')
    return render(request, 'main/home.html', context)

def articles(request):

    q = request.GET.get('q') if request.GET.get('q') != None else ''

    articles = Article.objects.filter(
        Q(category__icontains = q) |
        Q(title__icontains = q) |
        Q(description__icontains = q) |
        Q(author__username__icontains = q) 
        )

    article_count = articles.count()
    context= {'articles':articles, 'article_count':article_count}

    # messages.info(request, 'Three credits remain in your account.')
    return render(request, 'main/articles.html', context)

def article(request, pk):
    article = Article.objects.get(id=pk)
    comments = article.comment_set.all().order_by('-date_created')
   
    if request.method == 'POST':
        comment = Comment.objects.create(
            author = request.user,
            article = article,
            body = request.POST.get('body')
        )
        return redirect('article', pk=article.id)
        
    article.views = F('views') + 1
    article.save(update_fields=['views'])

    context = {'article': article, 'comments':comments}
    return render(request, 'main/article.html', context)


@login_required(login_url='login')
def createArticle(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles')
        
    context = {'form':form}
    return render(request, 'main/article_form.html', context )


@login_required(login_url='login')
def updateArticle(request, pk):
    article = Article.objects.get(id=pk)
    form = ArticleForm(instance=article)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article', pk=article.id)
    context = {'form':form}
    return render(request, 'main/article_form.html', context )


@login_required(login_url='login')
def deleteArticle(request, pk):
    article = Article.objects.get(id=pk)
    if request.method == "POST":
        article.delete()
        return redirect('articles')

    context= {'item': article}
    return render(request, 'main/delete.html', context )


@login_required(login_url='login')
def deleteComment(request, pk):
    comment = Comment.objects.get(id=pk)
    if request.method == "POST":
        comment.delete()
        return redirect('articles')

    context= {'item': comment}
    return render(request, 'main/delete.html', context )

