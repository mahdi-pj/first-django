from django.shortcuts import render, get_object_or_404,redirect
from .models import Topic,Post,Board,User


def home(request):
    return render(request,'first.html')



def board(request):
    boards = Board.objects.all()
    return render(request,'home.html',{'boards':boards})


def board_topics(request,pk):
   # try:
      #  board=Board.objects.get(pk=pk)
    #except board.DoesNotExist:
     #   raise Http404
    board = get_object_or_404 ( Board , pk=pk )
    return render(request,'board.html',{'board':board})



def new_topics(request,pk):
    board=get_object_or_404(Board,pk=pk)


    if request.method== "POST":
        subject=request.POST['subject']
        message=request.POST['message']

        user = User.objects.first()

        topic = Topic.objects.create(
            subject=subject,
            board=board,
            starter=user
        )

        post = Post.objects.create(
            message=message,
            topic=topic,
            created_by=user
        )
        return redirect('board_topics',pk=board.pk)

    return render(request,'new_topics.html',{'board':board})