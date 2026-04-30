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
            return redirect('/')
        else:
            messages.error(request, "Username/Email atau Password salah.")

    return render(request, 'login.html')

def logout_view(request):
    request.session.flush()
    messages.success(request, "Anda telah berhasil logout.")
    return redirect('login')

def register_role_view(request):
    if request.session.get('user_id'):
        return redirect('/')
    return render(request, 'register_role.html')

def register_customer_view(request):
    if request.session.get('user_id'):
        return redirect('/')
    if request.method == 'POST':
        full_name    = request.POST.get('full_name', '').strip()
        email        = request.POST.get('email', '').strip()
        phone        = request.POST.get('phone', '').strip()
        username     = request.POST.get('username', '').strip()
        password     = request.POST.get('password', '')
        confirm_pass = request.POST.get('confirm_password', '')
        agree        = request.POST.get('agree')
        errors = []
        if not all([full_name, email, phone, username, password, confirm_pass]):
            errors.append("Semua field wajib diisi.")
        if password != confirm_pass:
            errors.append("Password dan konfirmasi password tidak cocok.")
        if len(password) < 6:
            errors.append("Password minimal 6 karakter.")
        if not agree:
            errors.append("Anda harus menyetujui Syarat & Ketentuan.")
        if any(u['username'] == username for u in STATIC_USERS):
            errors.append("Username sudah digunakan.")
        if errors:
            for e in errors:
                messages.error(request, e)
            return render(request, 'register_customer.html', {'form_data': request.POST})
        STATIC_USERS.append({
            'id': str(len(STATIC_USERS) + 1),
            'username': username, 'email': email, 'password': password,
            'role': 'Customer', 'full_name': full_name, 'phone': phone,
        })
        messages.success(request, "Akun berhasil dibuat! Silakan login.")
        return redirect('login')
    return render(request, 'register_customer.html')

def register_organizer_view(request):
    if request.session.get('user_id'):
        return redirect('/')
    if request.method == 'POST':
        organizer_name = request.POST.get('organizer_name', '').strip()
        email          = request.POST.get('email', '').strip()
        phone          = request.POST.get('phone', '').strip()
        username       = request.POST.get('username', '').strip()
        password       = request.POST.get('password', '')
        confirm_pass   = request.POST.get('confirm_password', '')
        agree          = request.POST.get('agree')
        errors = []
        if not all([organizer_name, email, phone, username, password, confirm_pass]):
            errors.append("Semua field wajib diisi.")
        if password != confirm_pass:
            errors.append("Password dan konfirmasi password tidak cocok.")
        if len(password) < 6:
            errors.append("Password minimal 6 karakter.")
        if not agree:
            errors.append("Anda harus menyetujui Syarat & Ketentuan.")
        if any(u['username'] == username for u in STATIC_USERS):
            errors.append("Username sudah digunakan.")
        if errors:
            for e in errors:
                messages.error(request, e)
            return render(request, 'register_organizer.html', {'form_data': request.POST})
        STATIC_USERS.append({
            'id': str(len(STATIC_USERS) + 1),
            'username': username, 'email': email, 'password': password,
            'role': 'Organizer', 'organizer_name': organizer_name, 'phone': phone,
        })
        messages.success(request, "Akun berhasil dibuat! Silakan login.")
        return redirect('login')
    return render(request, 'register_organizer.html')

def register_admin_view(request):
    if request.session.get('user_id'):
        return redirect('/')
    if request.method == 'POST':
        username     = request.POST.get('username', '').strip()
        password     = request.POST.get('password', '')
        confirm_pass = request.POST.get('confirm_password', '')
        agree        = request.POST.get('agree')
        errors = []
        if not all([username, password, confirm_pass]):
            errors.append("Semua field wajib diisi.")
        if password != confirm_pass:
            errors.append("Password dan konfirmasi password tidak cocok.")
        if len(password) < 6:
            errors.append("Password minimal 6 karakter.")
        if not agree:
            errors.append("Anda harus menyetujui Syarat & Ketentuan.")
        if any(u['username'] == username for u in STATIC_USERS):
            errors.append("Username sudah digunakan.")
        if errors:
            for e in errors:
                messages.error(request, e)
            return render(request, 'register_admin.html', {'form_data': request.POST})
        STATIC_USERS.append({
            'id': str(len(STATIC_USERS) + 1),
            'username': username, 'email': '', 'password': password, 'role': 'Admin',
        })
        messages.success(request, "Akun berhasil dibuat! Silakan login.")
        return redirect('login')
    return render(request, 'register_admin.html')