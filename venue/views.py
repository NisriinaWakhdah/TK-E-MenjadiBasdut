import uuid
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404

# Mock Data Venue
STATIC_VENUES = [
    {'id': 'V001', 'name': 'Gelora Bung Karno', 'city': 'Jakarta Pusat', 'address': 'Jl. Pintu Satu Senayan', 'capacity': 77000},
    {'id': 'V002', 'name': 'ICE BSD', 'city': 'Tangerang', 'address': 'Jl. BSD Grand Boulevard', 'capacity': 10000},
]

def venue_list(request):
    # R - Semua: Siapapun bisa lihat daftar venue
    sorted_venues = sorted(STATIC_VENUES, key=lambda x: x['name'])
    context = {
        'venues': sorted_venues
    }
    return render(request, 'venue_list.html', context)

def venue_create(request):
    # C - Admin, Organizer
    role = request.session.get('role')
    request.session['role'] = 'admin'
    if role not in ['admin', 'organizer']:
        messages.error(request, "Hanya Admin dan Organizer yang dapat menambahkan Venue.")
        return redirect('venue_list')
        
    if request.method == 'POST':
        new_id = f"V{str(uuid.uuid4())[:4].upper()}"
        STATIC_VENUES.append({
            'id': new_id,
            'name': request.POST.get('name'),
            'city': request.POST.get('city'),
            'address': request.POST.get('address'),
            'capacity': int(request.POST.get('capacity', 0))
        })
        messages.success(request, "Venue berhasil ditambahkan.")
        return redirect('venue_list')
        
    return render(request, 'venue_form.html')

def venue_update(request, venue_id):
    # U - Admin, Organizer
    role = request.session.get('role')
    if role not in ['admin', 'organizer']:
        messages.error(request, "Hanya Admin dan Organizer yang dapat mengubah Venue.")
        return redirect('venue_list')
        
    venue = next((v for v in STATIC_VENUES if v['id'] == venue_id), None)
    if not venue:
        raise Http404("Venue tidak ditemukan")

    if request.method == 'POST':
        venue['name'] = request.POST.get('name')
        venue['city'] = request.POST.get('city')
        venue['address'] = request.POST.get('address')
        venue['capacity'] = int(request.POST.get('capacity', 0))
            
        messages.success(request, "Data Venue berhasil diperbarui.")
        return redirect('venue_list')
        
    context = {
        'venue': venue
    }
    return render(request, 'venue_form.html', context)

def venue_delete(request, venue_id):
    # D - Admin, Organizer
    role = request.session.get('role')
    if role not in ['admin', 'organizer']:
        messages.error(request, "Hanya Admin dan Organizer yang dapat menghapus Venue.")
        return redirect('venue_list')
        
    if request.method == 'POST':
        global STATIC_VENUES
        STATIC_VENUES[:] = [v for v in STATIC_VENUES if v['id'] != venue_id]
        messages.success(request, "Venue berhasil dihapus.")
        
    return redirect('venue_list')