from django.shortcuts import render, redirect
from django.contrib import messages

STATIC_USERS = [
    {'id': '1', 'username': 'admin', 'email': 'admin@ui.ac.id', 'password': 'password123', 'role': 'Admin'},
    {'id': '2', 'username': 'organizer', 'email': 'organizer@ui.ac.id', 'password': 'password123', 'role': 'Organizer'},
    {'id': '3', 'username': 'customer', 'email': 'customer@ui.ac.id', 'password': 'password123', 'role': 'Customer'},
]

def login_view(request):
    if request.session.get('user_id'):
        return redirect('/')
        
    if request.method == 'POST':
        username_input = request.POST.get('username')
        password_input = request.POST.get('password')
        
        user = next((u for u in STATIC_USERS if (u['username'] == username_input or u['email'] == username_input) and u['password'] == password_input), None)
        
        if user:
            request.session['user_id'] = user['id']
            request.session['username'] = user['username']
            request.session['role'] = user['role'].lower()
            request.session['email'] = user['email']
            
            messages.success(request, f"Login berhasil! Selamat datang, {user['username']}.")
            return redirect('/') # Temp redirect to root since dashboard is handled elsewhere
        else:
            messages.error(request, "Username/Email atau Password salah.")
            
    return render(request, 'login.html')

def logout_view(request):
    request.session.flush()
    messages.success(request, "Anda telah berhasil logout.")
    return redirect('login')
