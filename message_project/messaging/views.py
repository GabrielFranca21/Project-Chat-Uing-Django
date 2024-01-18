from django.shortcuts import render, redirect
from django.views import View
from .models import User, Message
from .forms import MessageForm

class ChatView(View):
    template_name = 'messaging/chat.html'

    def get(self, request):
        users = User.objects.all()
        messages = Message.objects.all()
        form = MessageForm()
        return render(request, self.template_name, {'users': users, 'messages': messages, 'form': form})

    def post(self, request):
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chat')
        else:
            users = User.objects.all()
            messages = Message.objects.all()
            return render(request, self.template_name, {'users': users, 'messages': messages, 'form': form})

class ClearChatView(View):
    def post(self, request):
        Message.objects.all().delete()
        return redirect('chat')
