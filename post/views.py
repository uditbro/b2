from django.shortcuts import render, redirect
from django.http import JsonResponse
import requests
from .forms import ArticleForm
from .models import Article
from .serializers import ArticleSerializer

from django.contrib.auth.decorators import login_required
from django.http import Http404




@login_required
def article_form(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            article.save(using='mysql_db')
            return redirect('blog:topics')



    else:
        form = ArticleForm()
    return render(request, 'show/article_form.html', {'form': form})