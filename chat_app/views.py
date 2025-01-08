from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Message

def chat_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        content = request.POST.get('content')
        Message.objects.create(username=username, content=content)
        return redirect('chat')

    messages = Message.objects.all().order_by('-timestamp')
    return render(request, 'chat/chat.html', {'messages': messages})