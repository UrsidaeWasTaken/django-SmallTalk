from django.contrib import admin
from .models import ChatRoom, ChatMessage


# Register your models here.
admin.site.register(ChatMessage)
admin.site.register(ChatRoom)
