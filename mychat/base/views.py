from django.shortcuts import render
from agora_token_builder import RtcTokenBuilder 
from django.http import JsonResponse
import json
import random
import time 
from .models import RoomMembers
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def get_token(request) :
    appId = 'eb0aeda4ac5e426fb3c8dc2931ad2a76'
    appCertificate = '2cb5d71602db4d3fb0d76d48a1e7c81d'
    channelname = request.GET.get('channel')
    uid = random.randint(1, 230)
    expirationTimeInSeconds = 3600 * 24
    currentTimeStamp = time.time()
    previlegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1
    
    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelname, uid, role, previlegeExpiredTs) 
    return JsonResponse({'token' : token, 'uid':uid}, safe=False)
    
# Lobby Page View
def lobby(request) :
    return render(request, 'base/lobby.html')

# Room Page View
def room(request) :
    return render(request, 'base/room.html')

@csrf_exempt
def create_member(request) :
    data = json.loads(request.body)
    
    member, created = RoomMembers.objects.get_or_create (
        name = data['name'],
        uid = data['UID'],
        room_name = data['room_name']
    )
    
    return JsonResponse({'name' : data['name']}, safe = False)

def get_member(request) :
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')
    
    member = RoomMembers.objects.get(
        uid = uid,
        room_name = room_name
        )
    
    return JsonResponse({'name' : member.name}, safe=False)


@csrf_exempt
def delete_member(request) :
    data = json.loads(request.body)
    
    member = RoomMembers.objects.get(
        name = data['name'],
        uid = data['UID'],
        room_name = data['room_name'],
        )
    
    member.delete()
  
    return JsonResponse('Member Was Deleted!', safe = False)