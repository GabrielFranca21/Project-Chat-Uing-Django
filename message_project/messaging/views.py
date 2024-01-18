from django.shortcuts import render
from django.views import View
from .models import User, Message
class ChatView(View):
    template_name = 'messaging/chat.html'

    def get(self, request):
        users = User.objects.all()
        messages = Message.objects.all()
        return render(request, self.template_name, {'users': users, 'messages': messages})
