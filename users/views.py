from django.shortcuts import render, redirect
from django.contrib import messages

STATIC_USERS = [
    {'id': '1', 'username': 'admin', 'email': 'admin@ui.ac.id', 'password': 'password123', 'role': 'Admin'},
    {'id': '2', 'username': 'organizer', 'email': 'organizer@ui.ac.id', 'password': 'password123', 'role': 'Organizer'},
    {'id': '3', 'username': 'customer', 'email': 'customer@ui.ac.id', 'password': 'password123', 'role': 'Customer'},
]

def homepage_view(request):
    return render(request, 'homepage.html')

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

            display_name = user.get('organizer_name') or user.get('full_name') or user['username']
            request.session['display_name'] = display_name

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

from django.shortcuts import render

def admin_dashboard(request):
    # Data Dummy untuk Statistik Utama
    stats = {
        'total_pengguna': '2,543',
        'total_acara': 156,
        'omzet': '52.4M',
        'promo_aktif': 3,
    }

    # Data Dummy untuk Infrastruktur Venue
    venue_info = {
        'total_lokasi': 3,
        'reserved_seating': 2,
        'kapasitas_max': '1,000',
    }

    # Data Dummy untuk Marketing & Promosi
    marketing_info = {
        'promo_persentase': 1,
        'promo_nominal': 1,
        'total_penggunaan': 57,
    }

    context = {
        'stats': stats,
        'venue_info': venue_info,
        'marketing_info': marketing_info,
    }
    
    return render(request, 'dashboard_admin.html', context)

def organizer_dashboard(request):
    if request.session.get('role') != 'organizer':
        messages.error(request, "Anda tidak memiliki akses ke halaman ini.")
        return redirect('login')
    
    nama_user = request.session.get('display_name', 'Penyelenggara')

    stats = {
        'nama_organizer': nama_user,
        'acara_aktif': 3,
        'tiket_terjual': '1,243',
        'revenue': '4.8M',
        'venue_mitra': 3,
    }

    daftar_acara = [
        {
            'nama': 'Konser Melodi Senja',
            'status': 'LIVE',
            'persentase': '85%',
            'lokasi': 'Jakarta Convention Center'
        },
        {
            'nama': 'Festival Seni Budaya',
            'status': 'LIVE',
            'persentase': '85%',
            'lokasi': 'Taman Impian Jayakarta'
        },
        {
            'nama': 'Malam Akustik Bandung',
            'status': 'LIVE',
            'persentase': '85%',
            'lokasi': 'Bandung Hall Center'
        }
    ]

    context = {
        'stats': stats,
        'daftar_acara': daftar_acara,
    }
    
    return render(request, 'dashboard_organizer.html', context)

def customer_dashboard(request):
    if request.session.get('role') != 'customer':
        messages.error(request, "Anda tidak memiliki akses ke halaman ini.")
        return redirect('login')

    nama_user = request.session.get('display_name', 'Customer')

    stats = {
        'nama_customer': nama_user,
        'tiket_aktif': 2,
        'acara_diikuti': 12,
        'kode_promo': 3,
        'total_belanja': '1.6M',
    }
    incoming_tickets = [
        {
            'nama': 'Konser Melodi Senja',
            'kategori': 'WVIP',
            'tanggal': '15 Mei 2024',
            'lokasi': 'Jakarta Convention Center'
        },
        {
            'nama': 'Festival Seni Budaya',
            'kategori': 'GENERAL',
            'tanggal': '22 Mei 2024',
            'lokasi': 'Taman Impian Jayakarta'
        }
    ]

    context = {
        'stats': stats,
        'tiket_mendatang': incoming_tickets,
    }
    
    return render(request, 'dashboard_customer.html', context)

def profile_customer(request):
    user_id = request.session.get('user_id')

    if not user_id or request.session.get('role') != 'customer':
        messages.error(request, "Silakan login sebagai Customer untuk mengakses profil.")
        return redirect('login')
    
    user_data = next((u for u in STATIC_USERS if u['id'] == user_id), None)

    if not user_data:
        messages.error(request, "Data user tidak ditemukan.")
        return redirect('login')

    if request.method == 'POST':
        action = request.POST.get('action')

        # =========================
        # UPDATE USERNAME
        # =========================
        if action == 'update_username':
            new_username = request.POST.get('username', '').strip()

            if not new_username:
                messages.error(request, "Username tidak boleh kosong.")
            
            elif any(u['username'] == new_username and u['id'] != user_id for u in STATIC_USERS):
                messages.error(request, "Username sudah digunakan.")
            
            else:
                user_data['username'] = new_username
                request.session['username'] = new_username
                request.session['display_name'] = new_username 
                messages.success(request, "Username berhasil diperbarui.")

            return redirect('profile_customer')  

        # =========================
        # UPDATE PASSWORD
        # =========================
        elif action == 'update_password':
            old_pass = request.POST.get('old_password', '')
            new_pass = request.POST.get('new_password', '')
            confirm_pass = request.POST.get('confirm_password', '')

            if not all([old_pass, new_pass, confirm_pass]):
                messages.error(request, "Semua field password harus diisi.")

            elif old_pass != user_data['password']:
                messages.error(request, "Password lama salah.")

            elif new_pass != confirm_pass:
                messages.error(request, "Konfirmasi password tidak cocok.")

            elif len(new_pass) < 6:
                messages.error(request, "Password minimal 6 karakter.")

            else:
                user_data['password'] = new_pass
                messages.success(request, "Password berhasil diperbarui.")

            return redirect('profile_customer')

    return render(request, 'profile_customer.html', {
        'user': user_data
    })

def profile_organizer(request):
    user_id = request.session.get('user_id')

    if not user_id or request.session.get('role') != 'organizer':
        messages.error(request, "Silakan login sebagai Organizer untuk mengakses profil.")
        return redirect('login')
    
    # Cari data user di STATIC_USERS
    user_data = next((u for u in STATIC_USERS if u['id'] == user_id), None)

    if request.method == 'POST':
        action = request.POST.get('action')

        # =========================
        # UPDATE INFORMASI PROFIL
        # =========================
        if action == 'update_profile':
            new_name = request.POST.get('organizer_name', '').strip()
            new_email = request.POST.get('email', '').strip()

            if not new_name or not new_email:
                messages.error(request, "Nama Organizer dan Email tidak boleh kosong.")
            else:
                user_data['organizer_name'] = new_name
                user_data['email'] = new_email

                request.session['display_name'] = new_name
                request.session['email'] = new_email
                messages.success(request, "Profil berhasil diperbarui.")
            return redirect('profile_organizer')

        # =========================
        # UPDATE PASSWORD
        # =========================
        elif action == 'update_password':
            old_pass = request.POST.get('old_password', '')
            new_pass = request.POST.get('new_password', '')
            confirm_pass = request.POST.get('confirm_password', '')

            if old_pass != user_data['password']:
                messages.error(request, "Password lama salah.")
            elif new_pass != confirm_pass:
                messages.error(request, "Konfirmasi password tidak cocok.")
            elif len(new_pass) < 6:
                messages.error(request, "Password minimal 6 karakter.")
            else:
                user_data['password'] = new_pass
                messages.success(request, "Password berhasil diperbarui.")
            return redirect('profile_organizer')

    return render(request, 'profile_organizer.html', {'user': user_data})

def profile_admin(request):
    user_id = request.session.get('user_id')

    if not user_id or request.session.get('role') != 'admin':
        messages.error(request, "Silakan login sebagai Admin untuk mengakses profil.")
        return redirect('login')

    user_data = next((u for u in STATIC_USERS if u['id'] == user_id), None)

    if not user_data:
        messages.error(request, "Data user tidak ditemukan.")
        return redirect('login')
    
    if request.method == 'POST':
        action = request.POST.get('action')

        # =========================
        # UPDATE USERNAME
        # =========================
        if action == 'update_username':
            new_username = request.POST.get('username', '').strip()

            if not new_username:
                messages.error(request, "Username tidak boleh kosong.")

            elif any(u['username'] == new_username and u['id'] != user_id for u in STATIC_USERS):
                messages.error(request, "Username sudah digunakan.")

            else:
                user_data['username'] = new_username
                request.session['username'] = new_username
                request.session['display_name'] = new_username
                messages.success(request, "Username berhasil diperbarui.")

            return redirect('profile_admin')

        # =========================
        # UPDATE PASSWORD
        # =========================
        elif action == 'update_password':
            old_pass = request.POST.get('old_password', '')
            new_pass = request.POST.get('new_password', '')
            confirm_pass = request.POST.get('confirm_password', '')

            if not all([old_pass, new_pass, confirm_pass]):
                messages.error(request, "Semua field password harus diisi.")

            elif old_pass != user_data['password']:
                messages.error(request, "Password lama salah.")

            elif new_pass != confirm_pass:
                messages.error(request, "Konfirmasi password tidak cocok.")

            elif len(new_pass) < 6:
                messages.error(request, "Password minimal 6 karakter.")

            else:
                user_data['password'] = new_pass
                messages.success(request, "Password berhasil diperbarui.")

            return redirect('profile_admin')

    return render(request, 'profile_admin.html', {
        'user': user_data
    })