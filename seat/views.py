import uuid
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404
from venue.views import STATIC_VENUES

STATIC_VENUES = [
    {'id': 'V001', 'name': 'Gelora Bung Karno', 'capacity': 50000, 'city': 'Jakarta', 'address': 'Jl. Pintu Satu Senayan'},
    {'id': 'V002', 'name': 'Jakarta Convention Center', 'capacity': 1000, 'city': 'Jakarta', 'address': 'Jl. Gatot Subroto No.1'},
    {'id': 'V003', 'name': 'Taman Impian Jayakarta', 'capacity': 500, 'city': 'Jakarta Utara', 'address': 'Jl. Lodan Timur No.7'},
    {'id': 'V004', 'name': 'Bandung Hall Center', 'capacity': 800, 'city': 'Bandung', 'address': 'Jl. Asia Afrika Bandung'},
    {'id': 'V005', 'name': 'ICE BSD', 'capacity': 5000, 'city': 'Tangerang', 'address': 'Jl. BSD Grand Boulevard'},
]

STATIC_SEATS = [
    {'id': 'seat_01', 'section': 'VIP', 'row': 'A', 'number': '1', 'venue_id': 'V001', 'venue': 'Gelora Bung Karno', 'status': 'Terisi'},
    {'id': 'seat_02', 'section': 'VIP', 'row': 'A', 'number': '2', 'venue_id': 'V001', 'venue': 'Gelora Bung Karno', 'status': 'Tersedia'},
    {'id': 'seat_03', 'section': 'VIP', 'row': 'A', 'number': '3', 'venue_id': 'V001', 'venue': 'Gelora Bung Karno', 'status': 'Tersedia'},
    {'id': 'seat_04', 'section': 'VIP', 'row': 'A', 'number': '4', 'venue_id': 'V001', 'venue': 'Gelora Bung Karno', 'status': 'Terisi'},
    {'id': 'seat_05', 'section': 'VIP', 'row': 'A', 'number': '5', 'venue_id': 'V001', 'venue': 'Gelora Bung Karno', 'status': 'Tersedia'},
    {'id': 'seat_06', 'section': 'Reguler', 'row': 'B', 'number': '1', 'venue_id': 'V001', 'venue': 'Gelora Bung Karno', 'status': 'Tersedia'},
    {'id': 'seat_07', 'section': 'Reguler', 'row': 'B', 'number': '2', 'venue_id': 'V001', 'venue': 'Gelora Bung Karno', 'status': 'Terisi'},
    {'id': 'seat_08', 'section': 'Reguler', 'row': 'B', 'number': '3', 'venue_id': 'V001', 'venue': 'Gelora Bung Karno', 'status': 'Tersedia'},
    {'id': 'seat_09', 'section': 'Reguler', 'row': 'B', 'number': '4', 'venue_id': 'V001', 'venue': 'Gelora Bung Karno', 'status': 'Tersedia'},
    {'id': 'seat_10', 'section': 'Reguler', 'row': 'B', 'number': '5', 'venue_id': 'V001', 'venue': 'Gelora Bung Karno', 'status': 'Terisi'},
    
    {'id': 'seat_11', 'section': 'WVIP', 'row': 'A', 'number': '1', 'venue_id': 'V002', 'venue': 'Jakarta Convention Center', 'status': 'Terisi'},
    {'id': 'seat_12', 'section': 'WVIP', 'row': 'A', 'number': '2', 'venue_id': 'V002', 'venue': 'Jakarta Convention Center', 'status': 'Tersedia'},
    {'id': 'seat_13', 'section': 'WVIP', 'row': 'A', 'number': '3', 'venue_id': 'V002', 'venue': 'Jakarta Convention Center', 'status': 'Tersedia'},
    {'id': 'seat_14', 'section': 'WVIP', 'row': 'A', 'number': '4', 'venue_id': 'V002', 'venue': 'Jakarta Convention Center', 'status': 'Tersedia'},
    {'id': 'seat_15', 'section': 'WVIP', 'row': 'A', 'number': '5', 'venue_id': 'V002', 'venue': 'Jakarta Convention Center', 'status': 'Terisi'},
    {'id': 'seat_16', 'section': 'Category 1', 'row': 'B', 'number': '1', 'venue_id': 'V002', 'venue': 'Jakarta Convention Center', 'status': 'Tersedia'},
    {'id': 'seat_17', 'section': 'Category 1', 'row': 'B', 'number': '2', 'venue_id': 'V002', 'venue': 'Jakarta Convention Center', 'status': 'Tersedia'},
    {'id': 'seat_18', 'section': 'Category 1', 'row': 'B', 'number': '3', 'venue_id': 'V002', 'venue': 'Jakarta Convention Center', 'status': 'Terisi'},
    {'id': 'seat_19', 'section': 'Category 1', 'row': 'B', 'number': '4', 'venue_id': 'V002', 'venue': 'Jakarta Convention Center', 'status': 'Tersedia'},
    {'id': 'seat_20', 'section': 'Category 1', 'row': 'B', 'number': '5', 'venue_id': 'V002', 'venue': 'Jakarta Convention Center', 'status': 'Tersedia'},
    
    {'id': 'seat_21', 'section': 'Festival', 'row': 'A', 'number': '1', 'venue_id': 'V003', 'venue': 'Taman Impian Jayakarta', 'status': 'Terisi'},
    {'id': 'seat_22', 'section': 'Festival', 'row': 'A', 'number': '2', 'venue_id': 'V003', 'venue': 'Taman Impian Jayakarta', 'status': 'Tersedia'},
    {'id': 'seat_23', 'section': 'Festival', 'row': 'A', 'number': '3', 'venue_id': 'V003', 'venue': 'Taman Impian Jayakarta', 'status': 'Tersedia'},
    {'id': 'seat_24', 'section': 'Festival', 'row': 'A', 'number': '4', 'venue_id': 'V003', 'venue': 'Taman Impian Jayakarta', 'status': 'Terisi'},
    {'id': 'seat_25', 'section': 'Festival', 'row': 'A', 'number': '5', 'venue_id': 'V003', 'venue': 'Taman Impian Jayakarta', 'status': 'Tersedia'},
    
    {'id': 'seat_26', 'section': 'Tribune', 'row': 'A', 'number': '1', 'venue_id': 'V004', 'venue': 'Bandung Hall Center', 'status': 'Tersedia'},
    {'id': 'seat_27', 'section': 'Tribune', 'row': 'A', 'number': '2', 'venue_id': 'V004', 'venue': 'Bandung Hall Center', 'status': 'Tersedia'},
    {'id': 'seat_28', 'section': 'Tribune', 'row': 'A', 'number': '3', 'venue_id': 'V004', 'venue': 'Bandung Hall Center', 'status': 'Terisi'},
    {'id': 'seat_29', 'section': 'Tribune', 'row': 'A', 'number': '4', 'venue_id': 'V004', 'venue': 'Bandung Hall Center', 'status': 'Tersedia'},
    {'id': 'seat_30', 'section': 'Tribune', 'row': 'A', 'number': '5', 'venue_id': 'V004', 'venue': 'Bandung Hall Center', 'status': 'Tersedia'},
]

def manage_seats(request):
    role = request.session.get('role', 'admin') # Default admin untuk testing
    is_admin_or_organizer = role in ['admin', 'organizer']

    # Ambil parameter search dan filter dari URL
    search_query = request.GET.get('q', '').lower()
    venue_filter = request.GET.get('venue_id', '')

    # Filter data kursi
    filtered_seats = STATIC_SEATS
    
    if venue_filter:
        filtered_seats = [seat for seat in filtered_seats if seat['venue_id'] == venue_filter]
        
    if search_query:
        filtered_seats = [
            seat for seat in filtered_seats 
            if search_query in seat['section'].lower() or 
               search_query in seat['row'].lower() or 
               search_query in seat['number'].lower()
        ]

    total_seats = len(filtered_seats)
    occupied = sum(1 for seat in filtered_seats if seat['status'] == 'Terisi')
    available = total_seats - occupied

    context = {
        'seats': sorted(filtered_seats, key=lambda x: (x['venue'], x['section'], x['row'])),
        'venues': STATIC_VENUES, 
        'total_seats': total_seats,
        'available': available,
        'occupied': occupied,
        'is_admin_or_organizer': is_admin_or_organizer,

        # Kirim kembali parameter ke template untuk mempertahankan state input
        'search_query': search_query,
        'current_venue_filter': venue_filter,
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