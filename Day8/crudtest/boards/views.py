from django.shortcuts import render, redirect
from .models import Board

# Create your views here.
# 게시글 제목, 내용, 작성자

def index(request) : 
    # Board 모델에 담긴 모든 글들을 가져와서 보여줌
    boards = Board.objects.all()
    context = {
        'boards' : boards
    }
    return render(request, 'index.html', context)

def new(request) :
    return render(request, 'new.html')

def create(request) : 
    title = request.GET['title']
    contents = request.GET['contents']
    creator = request.GET['creator']
    
    new_board = Board(title=title, contents=contents, creator=creator)
    #데이터 베이스에 저장
    #new_board.save() save까지 한번에 

    new_board = Board.objects.create(title=title, contents=contents, creator=creator)
    return redirect(f'/boards/{new_board.id}')

def show(request, id) :
    # 값을 찾는것 filter
    board = Board.objects.get(id=id)
    context = {
        'board' : board
    }
    return render(request, 'show.html', context)

def edit(request, id):
    # 원래 있던 내용이 들어있는 Form
    board = Board.objects.get(id=id)
    context = {
        'board' : board
    }
    return render(request, 'edit.html', context)

# 원래 있던 내용을 바꿔서 해당 row에 삽입
def update(request, id):
    # 실제로 update가 일어나는 곳
    board = Board.objects.get(id=id)
    title = request.GET['title']
    contents = request.GET['contents']
    
    board.title = title
    board.contents = contents
    board.save()

    context = {
        'board' : board
    }    
    return redirect(f'/boards/{board.id}')

def delete(request,id):
    board = Board.objects.get(id=id)
    board.delete()
    return redirect('/boards')