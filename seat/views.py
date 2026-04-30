import uuid
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404
from venue.views import STATIC_VENUES


STATIC_SEATS = [
    {'id': '1', 'section': 'WVIP', 'row': 'A', 'number': '1', 'venue_id': 'V001', 'venue': 'Gelora Bung Karno', 'status': 'Terisi'},
    {'id': '2', 'section': 'WVIP', 'row': 'A', 'number': '2', 'venue_id': 'V001', 'venue': 'Gelora Bung Karno', 'status': 'Tersedia'},
]

def manage_seats(request):
    role = request.session.get('role', 'admin') # Default admin untuk testing
    is_admin_or_organizer = role in ['admin', 'organizer']
    
    total_seats = len(STATIC_SEATS)
    occupied = sum(1 for seat in STATIC_SEATS if seat['status'] == 'Terisi')
    available = total_seats - occupied

    context = {
        'seats': sorted(STATIC_SEATS, key=lambda x: (x['venue'], x['section'], x['row'])),
        'venues': STATIC_VENUES, 
        'total_seats': total_seats,
        'available': available,
        'occupied': occupied,
        'is_admin_or_organizer': is_admin_or_organizer,
    }
    return render(request, 'manage_seats.html', context)

def seat_create(request):
    if request.method == 'POST':
        venue_id = request.POST.get('venue_id')
        section = request.POST.get('section')
        row = request.POST.get('row')
        number = request.POST.get('number')
        
        venue = next((v for v in STATIC_VENUES if v['id'] == venue_id), None)
        STATIC_SEATS.append({
            'id': str(uuid.uuid4()),
            'section': section, 'row': row, 'number': number,
            'venue_id': venue_id, 'venue': venue['name'] if venue else "Unknown",
            'status': 'Tersedia'
        })
        messages.success(request, "Kursi berhasil ditambahkan.")
    return redirect('manage_seats')

def seat_update(request, seat_id):
    if request.method == 'POST':
        seat = next((s for s in STATIC_SEATS if s['id'] == seat_id), None)
        if seat:
            venue_id = request.POST.get('venue_id')
            seat['section'] = request.POST.get('section')
            seat['row'] = request.POST.get('row')
            seat['number'] = request.POST.get('number')
            seat['venue_id'] = venue_id
            
            venue = next((v for v in STATIC_VENUES if v['id'] == venue_id), None)
            if venue: seat['venue'] = venue['name']
            messages.success(request, "Data kursi berhasil diperbarui.")
    return redirect('manage_seats')

def seat_delete(request, seat_id):
    if request.method == 'POST':
        global STATIC_SEATS
        STATIC_SEATS = [s for s in STATIC_SEATS if s['id'] != seat_id]
        messages.success(request, "Kursi berhasil dihapus.")
    return redirect('manage_seats')