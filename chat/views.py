from django.http import HttpResponse
from django.db import IntegrityError
from django.shortcuts import render
from .models import ChatRoom as ChatRoomModel, ChatMessage as ChatMessageModel
from .forms import MessageForm


# Create your views here.
def room(request, room_id=None):
    if request.user.is_authenticated:
        user = request.user
        if not room_id:
            return HttpResponse('Failed')

        if request.method == 'POST':
            try:
                chatroom = ChatRoomModel.object.get(id=room_id)
            except ChatRoomModel.DoesNotExist:
                try:
                    chatroom = ChatRoomModel(id=room_id)
                    chatroom.save()
                except IntegrityError:
                    chatroom = ChatRoomModel.object.get(id=room_id)

            form = MessageForm(request.POST)
            if form.is_valid():
                msg = ChatMessageModel(room=chatroom, user=user)
                msg.text = form.cleaned_data['text']
                msg.save()
            else:
                return HttpResponse('Failed')

        msgs = []
        try:
            chatroom = ChatRoomModel.object.get(id=room_id)
            chat_msgs = ChatMessageModel.object.filter(room=chatroom).order_by('-date')[:50]
            for msg in reversed(chat_msgs):
                msgs.append(msg.to_dict())
        except ChatRoomModel.DoesNotExist:
            return HttpResponse('Failed')

        context = {}
        context['message_input'] = MessageForm
        context['room_id'] = room_id
        context['messages'] = msgs
        context['user'] = user
        return render(request, 'chat/chat.html', context)
    else:
        context = {}
        context['room_id'] = room_id or 'default'
        return HttpResponse('Failed')
