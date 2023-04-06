from django.shortcuts import render
from .models import Article
from .forms import ArticleForm
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def news_home(request):
    news = Article.objects.order_by('date')
    return render(request, 'news/news_home.html', {'news':news})
def create(request):
    form = ArticleForm()
    data = {
        'form': form
    }
    return render(request, 'news/create.html', data)



def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('news_home')
    else:
        form = UserCreationForm()
    return render(request, 'news/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('news/news_home')
    else:
        form = AuthenticationForm()
    return render(request, 'news/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('news/news_home')