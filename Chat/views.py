import json
from django.shortcuts import render, Http404
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from .models import Chat


@login_required(login_url='/login')
def index(request):
    return render(request, 'chat/index.html')


@login_required(login_url='/login')
def room(request, room_name):
    username = request.user.username
    chat = Chat.objects.filter(roomname=room_name)
    if chat.exists():
        context = {

            'room_name': room_name,
            'username': mark_safe(json.dumps(username))
        }

        return render(request, "chat/room.html", context)
    raise Http404()