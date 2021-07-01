from django.shortcuts import render, redirect
from .models import Track
from django.db.models import Q
from django.core.paginator import Paginator

def home(request):
    pop_tracks = Track.objects.filter(genre = 'POP')
    pop_paginator = Paginator(pop_tracks,4)
    p_page = request.GET.get('p_page')
    p_posts = pop_paginator.get_page(p_page)

    k_tracks = Track.objects.filter(genre = 'K-POP')
    k_paginator = Paginator(k_tracks,4)
    k_page = request.GET.get('k_page')
    k_posts = k_paginator.get_page(k_page)
    
    classic_tracks = Track.objects.filter(genre = 'classic')
    classic_paginator = Paginator(classic_tracks,4)
    c_page = request.GET.get('c_page')
    c_posts = classic_paginator.get_page(c_page)

    
    jazz_tracks = Track.objects.filter(genre = 'jazz')
    jazz_paginator = Paginator(jazz_tracks,4)
    j_page = request.GET.get('j_page')
    j_posts = jazz_paginator.get_page(j_page)

    return render(request, 'main.html',
    {'pop_list': p_posts,'k_list' : k_posts, 'classic_list': c_posts, 'jazz_list': j_posts})

# Create your views here.
