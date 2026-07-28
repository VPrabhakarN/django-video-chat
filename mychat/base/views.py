from django.shortcuts import render
from agora_token_builder import RtcTokenBuilder 
from django.http import JsonResponse
import random
import time 

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

