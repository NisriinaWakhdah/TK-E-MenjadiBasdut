import uuid
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404

# Mock Data Event
STATIC_EVENTS = [
    {
        'id': 'E001', 
        'title': 'Harmoni Jakarta 2026', 
        'date': '2026-08-15', 
        'time': '19:00',
        'venue_name': 'Gelora Bung Karno',
        'artists': 'Tulus, Raisa',
        'price_start': 500000,
        'category': 'Konser Musik'
    },
]

def event_list(request):
    # R - Semua: Siapapun bisa lihat daftar event (Jelajahi Acara)
    sorted_events = sorted(STATIC_EVENTS, key=lambda x: x['date'])
    context = {
        'events': sorted_events
    }
    return render(request, 'event_list.html', context)

def event_create(request):
    # C - Admin, Organizer
    request.session['role'] = 'admin'
    role = request.session.get('role')
    if role not in ['admin', 'organizer']:
        messages.error(request, "Hanya Admin dan Organizer yang dapat membuat Acara.")
        return redirect('event_list')
        
    if request.method == 'POST':
        new_id = f"E{str(uuid.uuid4())[:4].upper()}"
        STATIC_EVENTS.append({
            'id': new_id,
            'title': request.POST.get('title'),
            'date': request.POST.get('date'),
            'time': request.POST.get('time'),
            'venue_name': request.POST.get('venue_name', 'Venue Belum Ditentukan'),
            'artists': request.POST.get('artists'),
            'price_start': 0, # Nanti di TK04 akan dihitung dari minimum ticket category
            'category': 'Konser'
        })
        messages.success(request, "Acara berhasil dibuat.")
        return redirect('event_list')
        
    return render(request, 'event_form.html')

def event_update(request, event_id):
    # U - Admin, Organizer
    role = request.session.get('role')
    if role not in ['admin', 'organizer']:
        messages.error(request, "Hanya Admin dan Organizer yang dapat mengubah data Acara.")
        return redirect('event_list')
        
    event = next((e for e in STATIC_EVENTS if e['id'] == event_id), None)
    if not event:
        raise Http404("Acara tidak ditemukan")

    if request.method == 'POST':
        event['title'] = request.POST.get('title')
        event['date'] = request.POST.get('date')
        event['time'] = request.POST.get('time')
        event['artists'] = request.POST.get('artists')
            
        messages.success(request, "Data Acara berhasil diperbarui.")
        return redirect('event_list')
        
    context = {
        'event': event
    }
    return render(request, 'event_form.html', context)