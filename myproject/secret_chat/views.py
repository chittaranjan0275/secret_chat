import json
import secrets
import uuid

from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from .models import Chat_table

from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse, JsonResponse
import random
import string

from .models import Session, Chat_table


def index(request):
    return render(request, "index.html")


def get_random_string(length):
    # Random string with the combination of lower and upper case
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def generator(request):
    session_obj = Session.objects.create(link_slug=get_random_string(5),
                                         key=get_random_string(16))
    session_objs = []
    session_objs.append(session_obj)
    context = {'session_objs': session_objs}
    return render(request, "index.html", context)


def chat_begins(request, link_slug):
    if request.method == "GET":
        return render(request, "chat.html")

    if request.method == "POST":
        key = request.POST.get('key')
        print(key, link_slug)
        if Session.objects.filter(link_slug=link_slug, key=key).exists():

            chat_table_obj = Chat_table.objects.create(link_slug=link_slug, uuid=uuid.uuid1())

            chat_table_objs = []
            chat_table_objs.append(chat_table_obj)
            context = {'chat_table_objs': chat_table_objs}
            return render(request, "secret_chat.html", context)

        else:
            return HttpResponse("Wrong password entered !!! please enter correct password")


@csrf_exempt
def save_chat(request):
    print(request.body)
    read_dict = {}

    if request.method == 'POST':
        data = request.body.decode('utf-8')
        json_data = json.loads(data)
        print(json_data)
        Chat_table.objects.create(chat=json_data.get('chat'), uuid=json_data.get('uuid'),
                                  link_slug=json_data.get('link_slug'))
        read_dict = {'message': json_data.get('chat')}

        return HttpResponse(json.dumps(read_dict))


@csrf_exempt
def read_chat(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        json_data = json.loads(data)
        messages = Chat_table.objects.filter(link_slug=json_data.get('link_slug'), read=False).exclude(
            uuid=json_data.get('uuid'))
        msg1 = messages.first()
        if msg1 is None:
            read_dict = {'message': None}
            return HttpResponse(json.dumps(read_dict))

        for msg in messages:
            msg.read = True
            msg.save()
        read_dict = {'message': msg1.chat}
    return HttpResponse(json.dumps(read_dict))
