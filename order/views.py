from django.shortcuts import render

# These are temporary dummy views to support front-end implementation
def checkout_view(request):

    # Dummy data
    seats = ["A1", "A2", "A3", "A4", "A5", "B1", "B2", "B3", "B4", "B5", "C1", "C2"]

    context = {
        'seats': seats,
        'event_name': 'Konser Melodi Senja',
        'price_per_ticket': 250000,
        'quantity': 2,
        'total': 500000,
    }
    return render(request, 'checkout/customer_checkout.html', context)

def customer_orders_view(request):

    # Data dummy untuk simulasi database
    orders = [
        {
            'order_id': 'ord_001',
            'tanggal': '2024-04-10 14:32',
            'status': 'LUNAS',
            'total': '1,200,000'
        },
        {
            'order_id': 'ord_002',
            'tanggal': '2024-04-11 09:15',
            'status': 'LUNAS',
            'total': '150,000'
        },
    ]

    # Menghitung statistik dari dummy list
    lunas_count = sum(1 for o in orders if o['status'] == 'LUNAS')
    pending_count = sum(1 for o in orders if o['status'] == 'PENDING')

    context = {
        'orders': orders,
        'lunas_count': lunas_count,
        'pending_count': pending_count,
    }

    return render(request, 'orders/customer.html', context)

def organizer_orders_view(request):

    #Dummy data
    orders = [
        {'order_id': 'ord_001', 'pelanggan': 'Budi Santoso', 'tanggal': '2024-04-10 14:32', 'status': 'LUNAS', 'total': '1.200.000'},
        {'order_id': 'ord_002', 'pelanggan': 'Budi Santoso', 'tanggal': '2024-04-11 09:15', 'status': 'LUNAS', 'total': '150.000'},
        {'order_id': 'ord_003', 'pelanggan': 'Siti Rahayu', 'tanggal': '2024-04-12 18:44', 'status': 'PENDING', 'total': '1.500.000'},
    ]

    context = {
        'orders': orders,
        'total_order': 3,
        'lunas_count': 2,
        'pending_count': 1,
        'total_revenue': '1.350.000',
        'title': 'Dashboard Organizer - Daftar Order'
    }
    return render(request, 'orders/organizer.html', context)
