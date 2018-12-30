import json
from django.http import HttpResponse, HttpResponseNotAllowed
from django.db import IntegrityError
from django.shortcuts import render
from .models import ChatRoom as ChatRoomModel, ChatMessage as ChatMessageModel


# Create your views here.
def room(request, room_id=None):
    if request.user.is_authenticated:
        user = request.user
        if not room_id:
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
        context['room_id'] = room_id
        context['messages'] = msgs
        context['user'] = user
        return render(request, 'chat/chat.html', context)
    else:
        context = {}
        context['room_id'] = room_id or 'default'
        return HttpResponse('Failed')


def messages(request, room_id):
    if request.method == 'POST':
        try:
            chatroom = ChatRoomModel.object.get(id=room_id)
        except ChatRoomModel.DoesNotExist:
            try:
                chatroom = ChatRoomModel(id=room_id)
                chatroom.save()
            except IntegrityError:
                chatroom = ChatRoomModel.object.get(id=room_id)

        user = request.POST['user']
        text = request.POST['text']
        msg = ChatMessageModel(room=chatroom, user=user, message=text)
        msg.save()
        body = json.dumps(msg.to_dict())
        return HttpResponse(body, content_type='application/json')
    else:
        return HttpResponseNotAllowed(['POST'])
