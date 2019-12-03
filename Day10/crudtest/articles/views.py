from django.shortcuts import render, redirect
# 모델에 Article 클래스를 사용하겠다.
from . models import Article

# Create your views here.

def index(request):
    # Article Model에 있는 모든 Article을 불러옴
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'index.html', context)

def show(request, id):
    # Article Model에서 특정 id를 가진 하나의 Article 호출
    article = Article.objects.get(id=id)
    context = {
        'article' : article
    }
    return render(request, 'show.html', context)

def new(request):
    # 불러올 Article 없음
    if request.method  == 'POST':
        title = request.POST['title']
        contents = request.POST['contents']
        creator = request.POST['creator']
        article = Article()
        article.title = title
        article.contents = contents
        article.creator = creator
        article.save()
        return redirect('articles:show', article.id)
    else:
        return render(request, 'new.html')
'''
def create(request):
    # Article 생성
    title = request.GET['title']
    contents = request.GET['contents']
    creator = request.GET['creator']
    
    # 방법1
    # article = Article.objects.create
    # 방법2
    article = Article()
    article.title = title
    article.contents = contents
    article.creator = creator
    article.save()
    return redirect('articles:show', article.id)
'''
def edit(request , id):
    if request.method  == 'POST':
        article = Article.objects.get(id=id)
        # 기존 article 정보를 바꿔서 저장하는 부분
        title = request.POST['title']
        contents = request.POST['contents']
        creator = request.POST['creator']

        article.title = title
        article.contents = contents
        article.creator = creator
        article.save()
        return redirect('articles:show', article.id)
    
    else:
    # Article Model에 있는 특정 Article 호출
        article = Article.objects.get(id=id)
        context = {
            'article' : article
        }
        return render(request, 'edit.html' , context)
'''
def update(request, id):
    # Article Model에 있는 특정 Article 호출
    article = Article.objects.get(id=id)
    # 기존 article 정보를 바꿔서 저장하는 부분
    title = request.GET['title']
    contents = request.GET['contents']
    creator = request.GET['creator']
    
    article.title = title
    article.contents = contents
    article.creator = creator
    article.save()
    return redirect('articles:show', article.id)
'''

def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('articles:index')