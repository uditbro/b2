from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry, Picture
from .forms import TopicForm,EntryForm



def index(request):
    return render(request,'blog/index.html')

@login_required
def topics(request):
    topics = Topic.objects.filter(owner = request.user).order_by('date_added')
    context = {'topics': topics}

    return render(request,'blog/topics.html', context)

@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    #Make sure topic belongs to current user.
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}

    return render(request, 'blog/topic.html', context)

@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('blog:topics')
    
    context = {'form': form}
    return render(request, 'blog/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id = topic_id)

    if request.method != 'POST':
        form = EntryForm()

    else:
        form = EntryForm(data = request.POST)
        if form.is_valid():
            new_entry = form.save(commit = False)
            new_entry.text = topic
            new_entry.save()
            return redirect('blog:topic', topic_id = topic_id)
    
    context = {'topic': topic, 'form': form}
    return render(request, 'blog/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id = entry_id)
    topic = entry.text
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance = entry)
    
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:topic', topic_id = topic.id)
        
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'blog/edit_entry.html', context)