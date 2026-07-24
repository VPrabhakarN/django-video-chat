from django.shortcuts import render

# Create your views here.

# Lobby Page View
def lobby(request) :
    return render(request, 'base/lobby.html')

# Room Page View
def room(request) :
    return render(request, 'base/room.html')

