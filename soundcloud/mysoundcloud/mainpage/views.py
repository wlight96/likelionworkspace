from django.shortcuts import render, redirect
from .models import Track
from django.db.models import Q
from django.core.paginator import Paginator

def home(request):
    tracks = Track.objects
    track_list = Track.objects.all()
    pop_tracks = Track.objects.filter(genre = 'POP')
    k_tracks = Track.objects.filter(genre = 'K-POP')
    classic_tracks = Track.objects.filter(genre = 'classic')
    jazz_tracks = Track.objects.filter(genre = 'jazz')
    return render(request, 'main.html',
    {'pop_list': pop_tracks,'k_list' : k_tracks, 'classic_list': classic_tracks, 'jazz_list': jazz_tracks})

# Create your views here.
