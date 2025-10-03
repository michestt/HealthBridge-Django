from django.shortcuts import render, redirect
from .forms import *
# Create your views here.

def home(request):
    forums=forum.objects.all()
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={
        'forums':forums,
        'count':count,
        'discussions':discussions
        }

    return render(request,'dis_forum/home.html' ,context)


def addInForum(request):
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('discuss_home')
    context ={'form':form}
    return render(request,'dis_forum/addInForum.html',context)


def addInDiscussion(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('discuss_home')
    context ={'form':form}
    return render(request,'dis_forum/addInDiscussion.html',context)
