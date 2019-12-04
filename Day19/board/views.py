from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required

# 필요한 녀석들한테 달아준다
@login_required
def new_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('board:article_detail', article.id)
    else:  # GET
        form = ArticleForm()
    context = { 'form': form, }
    return render(request, 'board/article_form.html', context)


def article_list(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'board/article_list.html', context)


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    context = {'article': article}
    return render(request, 'board/article_detail.html', context)

@login_required
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('board:article_detail', article.id)
    else:  # GET
        form = ArticleForm(instance=article)
    context = { 'form': form, }
    return render(request, 'board/article_form.html', context)
