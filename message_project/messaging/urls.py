from django.urls import path
from .views import ChatView, ClearChatView

urlpatterns = [
    path('chat/', ChatView.as_view(), name='chat'),
    path('clear_chat/', ClearChatView.as_view(), name='clear_chat'),
]
