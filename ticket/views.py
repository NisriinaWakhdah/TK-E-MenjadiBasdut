import uuid
import datetime
from django.shortcuts import render, redirect
from django.contrib import messages

# Dummy Data
STATIC_ORDERS = [
    {'id': 'ord_001', 'customer_name': 'Budi Santoso', 'event_name': 'Konser Melodi Senja'},
    {'id': 'ord_002', 'customer_name': 'Siti Rahayu', 'event_name': 'Festival Seni Budaya'},
]

STATIC_CATEGORIES = [
    {'id': 'cat_01', 'event_name': 'Konser Melodi Senja', 'name': 'VIP', 'price': 750000, 'used': 3, 'quota': 150},
    {'id': 'cat_02', 'event_name': 'Festival Seni Budaya', 'name': 'General Admission', 'price': 150000, 'used': 1, 'quota': 500},
]

STATIC_SEATS_TICKET = [
    {'id': 'seat_01', 'label': 'VIP - Baris B, No. 1'},
    {'id': 'seat_02', 'label': 'Category 1 - Baris C, No. 1'},
]

# Dummy Data Ticket
STATIC_TICKETS = [
    {
        'id': 'TTK-EVT001-VIP-001', 'order_id': 'ord_001', 'customer_name': 'Budi Santoso',
        'event_name': 'Konser Melodi Senja', 'schedule': '2024-05-15 19:00',
        'venue': 'Jakarta Convention Center', 'seat': 'VIP - Baris B, No. 1', 'price': 750000, 'status': 'Valid'
    },
    {
        'id': 'TTK-EVT001-VIP-002', 'order_id': 'ord_001', 'customer_name': 'Budi Santoso',
        'event_name': 'Konser Melodi Senja', 'schedule': '2024-05-15 19:00',
        'venue': 'Jakarta Convention Center', 'seat': 'VIP - Baris B, No. 2', 'price': 750000, 'status': 'Terpakai'
    },
    {
        'id': 'TTK-EVT001-VIP-003', 'order_id': 'ord_001', 'customer_name': 'Budi Santoso',
        'event_name': 'Konser Melodi Senja', 'schedule': '2024-05-15 19:00',
        'venue': 'Jakarta Convention Center', 'seat': 'VIP - Baris B, No. 3', 'price': 750000, 'status': 'Valid'
    },
    {
        'id': 'TTK-EVT001-VIP-004', 'order_id': 'ord_001', 'customer_name': 'Budi Santoso',
        'event_name': 'Konser Melodi Senja', 'schedule': '2024-05-15 19:00',
        'venue': 'Jakarta Convention Center', 'seat': 'VIP - Baris B, No. 4', 'price': 750000, 'status': 'Valid'
    },
    {
        'id': 'TTK-EVT001-VIP-005', 'order_id': 'ord_001', 'customer_name': 'Budi Santoso',
        'event_name': 'Konser Melodi Senja', 'schedule': '2024-05-15 19:00',
        'venue': 'Jakarta Convention Center', 'seat': 'VIP - Baris B, No. 5', 'price': 750000, 'status': 'Terpakai'
    },
    {
        'id': 'TTK-EVT001-VIP-006', 'order_id': 'ord_001', 'customer_name': 'Budi Santoso',
        'event_name': 'Konser Melodi Senja', 'schedule': '2024-05-15 19:00',
        'venue': 'Jakarta Convention Center', 'seat': 'VIP - Baris C, No. 1', 'price': 750000, 'status': 'Valid'
    },
    {
        'id': 'TTK-EVT001-VIP-007', 'order_id': 'ord_001', 'customer_name': 'Budi Santoso',
        'event_name': 'Konser Melodi Senja', 'schedule': '2024-05-15 19:00',
        'venue': 'Jakarta Convention Center', 'seat': 'VIP - Baris C, No. 2', 'price': 750000, 'status': 'Valid'
    },
    {
        'id': 'TTK-EVT001-VIP-008', 'order_id': 'ord_001', 'customer_name': 'Budi Santoso',
        'event_name': 'Konser Melodi Senja', 'schedule': '2024-05-15 19:00',
        'venue': 'Jakarta Convention Center', 'seat': 'VIP - Baris C, No. 3', 'price': 750000, 'status': 'Terpakai'
    },
    {
        'id': 'TTK-EVT001-VIP-009', 'order_id': 'ord_001', 'customer_name': 'Budi Santoso',
        'event_name': 'Konser Melodi Senja', 'schedule': '2024-05-15 19:00',
        'venue': 'Jakarta Convention Center', 'seat': 'VIP - Baris C, No. 4', 'price': 750000, 'status': 'Valid'
    },
    {
        'id': 'TTK-EVT001-VIP-010', 'order_id': 'ord_001', 'customer_name': 'Budi Santoso',
        'event_name': 'Konser Melodi Senja', 'schedule': '2024-05-15 19:00',
        'venue': 'Jakarta Convention Center', 'seat': 'VIP - Baris C, No. 5', 'price': 750000, 'status': 'Valid'
    },

    {
        'id': 'TTK-EVT002-GEN-001', 'order_id': 'ord_002', 'customer_name': 'Siti Rahayu',
        'event_name': 'Festival Seni Budaya', 'schedule': '2024-05-22 10:00',
        'venue': 'Taman Impian Jayakarta', 'seat': 'Tanpa Kursi', 'price': 150000, 'status': 'Valid'
    },
    {
        'id': 'TTK-EVT002-GEN-002', 'order_id': 'ord_002', 'customer_name': 'Siti Rahayu',
        'event_name': 'Festival Seni Budaya', 'schedule': '2024-05-22 10:00',
        'venue': 'Taman Impian Jayakarta', 'seat': 'Tanpa Kursi', 'price': 150000, 'status': 'Valid'
    },
    {
        'id': 'TTK-EVT002-GEN-003', 'order_id': 'ord_002', 'customer_name': 'Siti Rahayu',
        'event_name': 'Festival Seni Budaya', 'schedule': '2024-05-22 10:00',
        'venue': 'Taman Impian Jayakarta', 'seat': 'Tanpa Kursi', 'price': 150000, 'status': 'Terpakai'
    },
    {
        'id': 'TTK-EVT002-GEN-004', 'order_id': 'ord_002', 'customer_name': 'Siti Rahayu',
        'event_name': 'Festival Seni Budaya', 'schedule': '2024-05-22 10:00',
        'venue': 'Taman Impian Jayakarta', 'seat': 'Tanpa Kursi', 'price': 150000, 'status': 'Valid'
    },
    {
        'id': 'TTK-EVT002-GEN-005', 'order_id': 'ord_002', 'customer_name': 'Siti Rahayu',
        'event_name': 'Festival Seni Budaya', 'schedule': '2024-05-22 10:00',
        'venue': 'Taman Impian Jayakarta', 'seat': 'Tanpa Kursi', 'price': 150000, 'status': 'Valid'
    },
    {
        'id': 'TTK-EVT002-GEN-006', 'order_id': 'ord_002', 'customer_name': 'Siti Rahayu',
        'event_name': 'Festival Seni Budaya', 'schedule': '2024-05-22 10:00',
        'venue': 'Taman Impian Jayakarta', 'seat': 'Tanpa Kursi', 'price': 150000, 'status': 'Terpakai'
    },
    {
        'id': 'TTK-EVT002-GEN-007', 'order_id': 'ord_002', 'customer_name': 'Siti Rahayu',
        'event_name': 'Festival Seni Budaya', 'schedule': '2024-05-22 10:00',
        'venue': 'Taman Impian Jayakarta', 'seat': 'Tanpa Kursi', 'price': 150000, 'status': 'Valid'
    },
    {
        'id': 'TTK-EVT002-GEN-008', 'order_id': 'ord_002', 'customer_name': 'Siti Rahayu',
        'event_name': 'Festival Seni Budaya', 'schedule': '2024-05-22 10:00',
        'venue': 'Taman Impian Jayakarta', 'seat': 'Tanpa Kursi', 'price': 150000, 'status': 'Valid'
    },
    {
        'id': 'TTK-EVT002-GEN-009', 'order_id': 'ord_002', 'customer_name': 'Siti Rahayu',
        'event_name': 'Festival Seni Budaya', 'schedule': '2024-05-22 10:00',
        'venue': 'Taman Impian Jayakarta', 'seat': 'Tanpa Kursi', 'price': 150000, 'status': 'Valid'
    },
    {
        'id': 'TTK-EVT002-GEN-010', 'order_id': 'ord_002', 'customer_name': 'Siti Rahayu',
        'event_name': 'Festival Seni Budaya', 'schedule': '2024-05-22 10:00',
        'venue': 'Taman Impian Jayakarta', 'seat': 'Tanpa Kursi', 'price': 150000, 'status': 'Valid'
    },
]

def manage_tickets(request):
    role = request.session.get('role', 'admin') # Role testing (admin, organizer, customer)
    logged_in_user = request.session.get('username', 'Budi Santoso') # Simulasi user
    
    can_create = role in ['admin', 'organizer']
    can_update_delete = role == 'admin'
    
    search_query = request.GET.get('q', '').lower()
    status_filter = request.GET.get('status', '')

    filtered_tickets = STATIC_TICKETS
    
    # Filter by Role
    if role == 'customer':
        filtered_tickets = [t for t in filtered_tickets if t['customer_name'] == logged_in_user]
        
    # Filter by Status
    if status_filter:
        filtered_tickets = [t for t in filtered_tickets if t['status'].lower() == status_filter.lower()]
        
    # Search Filter
    if search_query:
        filtered_tickets = [
            t for t in filtered_tickets 
            if search_query in t['id'].lower() or search_query in t['event_name'].lower()
        ]

    total_tickets = len(filtered_tickets)
    valid_tickets = sum(1 for t in filtered_tickets if t['status'] == 'Valid')
    used_tickets = sum(1 for t in filtered_tickets if t['status'] == 'Terpakai')

    context = {
        'tickets': filtered_tickets,
        'total_tickets': total_tickets,
        'valid_tickets': valid_tickets,
        'used_tickets': used_tickets,
        'can_create': can_create,
        'can_update_delete': can_update_delete,
        'role': role,
        'search_query': search_query,
        'current_status_filter': status_filter,
        # Untuk dropdown modal Create/Update
        'orders': STATIC_ORDERS,
        'categories': STATIC_CATEGORIES,
        'seats': STATIC_SEATS_TICKET,
    }
    return render(request, 'manage_tickets.html', context)

def ticket_create(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        category_id = request.POST.get('category_id')
        seat_label = request.POST.get('seat', 'Tanpa Kursi')
        
        # Cari detail berdasarkan ID
        order = next((o for o in STATIC_ORDERS if o['id'] == order_id), None)
        category = next((c for c in STATIC_CATEGORIES if c['id'] == category_id), None)
        
        if order and category:
            # Auto-generate Ticket Code
            unique_id = str(uuid.uuid4())[:8].upper()
            ticket_code = f"TTK-{unique_id}"
            
            STATIC_TICKETS.append({
                'id': ticket_code,
                'order_id': order['id'],
                'customer_name': order['customer_name'],
                'event_name': order['event_name'],
                'schedule': '2024-05-15 19:00', # Dummy schedule
                'venue': 'Jakarta Convention Center', # Dummy venue
                'seat': seat_label,
                'price': category['price'],
                'status': 'Valid'
            })
            messages.success(request, "Tiket berhasil dibuat.")
    return redirect('manage_tickets')

def ticket_update(request, ticket_id):
    if request.method == 'POST':
        ticket = next((t for t in STATIC_TICKETS if t['id'] == ticket_id), None)
        if ticket:
            ticket['status'] = request.POST.get('status')
            ticket['seat'] = request.POST.get('seat', ticket['seat'])
            messages.success(request, "Status dan kursi tiket berhasil diperbarui.")
    return redirect('manage_tickets')

def ticket_delete(request, ticket_id):
    if request.method == 'POST':
        global STATIC_TICKETS
        STATIC_TICKETS = [t for t in STATIC_TICKETS if t['id'] != ticket_id]
        messages.success(request, "Tiket berhasil dihapus.")
    return redirect('manage_tickets')