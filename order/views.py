from django.shortcuts import render

# Create your views here.
def checkout_view(request):
    seats = ["A1", "A2", "A3", "A4", "A5", "B1", "B2", "B3", "B4", "B5", "C1", "C2"]

    context = {
        'seats': seats,
        'event_name': 'Konser Melodi Senja',
        'price_per_ticket': 250000,
        'quantity': 2,
        'total': 500000,
    }
    return render(request, 'checkout/costumer_checkout.html', context)
