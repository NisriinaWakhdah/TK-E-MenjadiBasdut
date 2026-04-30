import uuid
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404

STATIC_ARTISTS = [
    {'id': str(uuid.uuid4()), 'name': 'Taylor Swift', 'genre': 'Pop'},
    {'id': str(uuid.uuid4()), 'name': 'Coldplay', 'genre': 'Alternative Rock'},
    {'id': str(uuid.uuid4()), 'name': 'Justin Bieber', 'genre': 'Pop'},
]

STATIC_EVENTS = [
    {'id': str(uuid.uuid4()), 'name': 'Eras Tour Jakarta'},
    {'id': str(uuid.uuid4()), 'name': 'Music of the Spheres'},
    {'id': str(uuid.uuid4()), 'name': 'JB World Tour'},
]

STATIC_CATEGORIES = [
    {'id': str(uuid.uuid4()), 'event_id': STATIC_EVENTS[0]['id'], 'name': 'VIP 1', 'price': 5000000, 'quota': 500, 'event_name': STATIC_EVENTS[0]['name']},
    {'id': str(uuid.uuid4()), 'event_id': STATIC_EVENTS[0]['id'], 'name': 'Festival A', 'price': 2500000, 'quota': 2000, 'event_name': STATIC_EVENTS[0]['name']},
    {'id': str(uuid.uuid4()), 'event_id': STATIC_EVENTS[1]['id'], 'name': 'Tribune 1', 'price': 1500000, 'quota': 1500, 'event_name': STATIC_EVENTS[1]['name']},
]

def artist_list(request):
    if not request.session.get('user_id'):
        return redirect('login')
        
    is_admin = request.session.get('role') == 'admin'
    sorted_artists = sorted(STATIC_ARTISTS, key=lambda x: x['name'])
        
    context = {
        'artists': sorted_artists,
        'is_admin': is_admin
    }
    return render(request, 'artist_list.html', context)

def artist_create(request):
    is_admin = request.session.get('role') == 'admin'
    if not is_admin:
        messages.error(request, "Hanya Admin yang dapat menambahkan artis.")
        return redirect('artist_list')
        
    if request.method == 'POST':
        name = request.POST.get('name')
        genre = request.POST.get('genre')
        new_id = str(uuid.uuid4())
        
        STATIC_ARTISTS.append({'id': new_id, 'name': name, 'genre': genre})
        
        messages.success(request, f"Artis {name} berhasil ditambahkan.")
        return redirect('artist_list')
        
    return render(request, 'artist_form.html')

def artist_update(request, artist_id):
    is_admin = request.session.get('role') == 'admin'
    if not is_admin:
        messages.error(request, "Hanya Admin yang dapat mengubah data artis.")
        return redirect('artist_list')
        
    artist = next((a for a in STATIC_ARTISTS if a['id'] == artist_id), None)
    if not artist:
        raise Http404("Artis tidak ditemukan")

    if request.method == 'POST':
        artist['name'] = request.POST.get('name')
        artist['genre'] = request.POST.get('genre')
            
        messages.success(request, "Data artis berhasil diperbarui.")
        return redirect('artist_list')
        
    context = {
        'artist': artist
    }
    return render(request, 'artist_form.html', context)

def artist_delete(request, artist_id):
    is_admin = request.session.get('role') == 'admin'
    if not is_admin:
        messages.error(request, "Hanya Admin yang dapat menghapus artis.")
        return redirect('artist_list')
        
    if request.method == 'POST':
        global STATIC_ARTISTS
        STATIC_ARTISTS[:] = [a for a in STATIC_ARTISTS if str(a['id']) != str(artist_id)]
        messages.success(request, "Artis berhasil dihapus.")
        
    return redirect('artist_list')

def ticket_category_list(request):
    if not request.session.get('user_id'):
        return redirect('login')
    is_admin_or_organizer = request.session.get('role') in ['admin', 'organizer']
    sorted_categories = sorted(STATIC_CATEGORIES, key=lambda x: (x['event_name'], x['name']))
        
    context = {
        'categories': sorted_categories,
        'is_admin_or_organizer': is_admin_or_organizer
    }
    return render(request, 'ticket_category_list.html', context)

def ticket_category_create(request):
    is_admin_or_organizer = request.session.get('role') in ['admin', 'organizer']
    if not is_admin_or_organizer:
        messages.error(request, "Hanya Admin dan Organizer yang dapat menambahkan kategori tiket.")
        return redirect('ticket_category_list')
        
    if request.method == 'POST':
        event_id = request.POST.get('event_id')
        name = request.POST.get('name')
        price = int(request.POST.get('price', 0))
        quota = int(request.POST.get('quota', 0))
        new_id = str(uuid.uuid4())
        
        event = next((e for e in STATIC_EVENTS if e['id'] == event_id), None)
        event_name = event['name'] if event else "Unknown Event"
        
        STATIC_CATEGORIES.append({
            'id': new_id, 
            'event_id': event_id, 
            'name': name, 
            'price': price, 
            'quota': quota,
            'event_name': event_name
        })
        
        messages.success(request, f"Kategori tiket {name} berhasil ditambahkan.")
        return redirect('ticket_category_list')
            
    sorted_events = sorted(STATIC_EVENTS, key=lambda x: x['name'])
    context = {
        'events': sorted_events,
        'form_errors': []
    }
    return render(request, 'ticket_category_form.html', context)

def ticket_category_update(request, category_id):
    is_admin_or_organizer = request.session.get('role') in ['admin', 'organizer']
    if not is_admin_or_organizer:
        messages.error(request, "Akses ditolak.")
        return redirect('ticket_category_list')
        
    category = next((c for c in STATIC_CATEGORIES if c['id'] == category_id), None)
    if not category:
        raise Http404("Kategori tidak ditemukan")
        
    if request.method == 'POST':
        event_id = request.POST.get('event_id')
        category['name'] = request.POST.get('name')
        category['price'] = int(request.POST.get('price', 0))
        category['quota'] = int(request.POST.get('quota', 0))
        category['event_id'] = event_id
        
        event = next((e for e in STATIC_EVENTS if e['id'] == event_id), None)
        if event:
            category['event_name'] = event['name']
            
        messages.success(request, "Kategori tiket berhasil diperbarui.")
        return redirect('ticket_category_list')
        
    sorted_events = sorted(STATIC_EVENTS, key=lambda x: x['name'])
    context = {
        'category': category,
        'events': sorted_events
    }
    return render(request, 'ticket_category_form.html', context)

def ticket_category_delete(request, category_id):
    is_admin_or_organizer = request.session.get('role') in ['admin', 'organizer']
    if not is_admin_or_organizer:
        messages.error(request, "Akses ditolak.")
        return redirect('ticket_category_list')
        
    if request.method == 'POST':
        global STATIC_CATEGORIES
        STATIC_CATEGORIES[:] = [c for c in STATIC_CATEGORIES if str(c['id']) != str(category_id)]
        messages.success(request, "Kategori tiket berhasil dihapus.")
        
    return redirect('ticket_category_list')