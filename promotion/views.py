from django.shortcuts import render

def promotion_management(request):
    # Simulasi data dari database
    promosi_list = [
        {
            'kode': 'TIKTAK20',
            'tipe': 'PERSENTASE',
            'nilai': '20%',
            'mulai': '2024-01-01',
            'berakhir': '2024-12-31',
            'terpakai': 45,
            'kuota': 100,
        },
        {
            'kode': 'HEMAT50K',
            'tipe': 'NOMINAL',
            'nilai': 'Rp 50.000',
            'mulai': '2024-01-01',
            'berakhir': '2024-12-31',
            'terpakai': 12,
            'kuota': 50,
        },
        {
            'kode': 'NEWUSER30',
            'tipe': 'PERSENTASE',
            'nilai': '30%',
            'mulai': '2024-03-01',
            'berakhir': '2024-06-30',
            'terpakai': 87,
            'kuota': 200,
        },
    ]

    # Simulasi Role Check (Ubah menjadi False untuk melihat tampilan Guest/Customer)
    is_admin = True 

    # Perhitungan Statistik Ringkasan
    stats = {
        'total_promo': len(promosi_list),
        'total_penggunaan': sum(p['terpakai'] for p in promosi_list),
        'total_persentase': len([p for p in promosi_list if p['tipe'] == 'PERSENTASE'])
    }

    context = {
        'promosi': promosi_list,
        'is_admin': is_admin,
        'stats': stats
    }
    
    return render(request, 'promotion_list.html', context)

def admin_promotion_management(request):
    # Simulasi data dari database
    promosi_list = [
        {
            'kode': 'TIKTAK20',
            'tipe': 'PERSENTASE',
            'nilai': '20%',
            'mulai': '2024-01-01',
            'berakhir': '2024-12-31',
            'terpakai': 45,
            'kuota': 100,
        },
        {
            'kode': 'HEMAT50K',
            'tipe': 'NOMINAL',
            'nilai': 'Rp 50.000',
            'mulai': '2024-01-01',
            'berakhir': '2024-12-31',
            'terpakai': 12,
            'kuota': 50,
        },
        {
            'kode': 'NEWUSER30',
            'tipe': 'PERSENTASE',
            'nilai': '30%',
            'mulai': '2024-03-01',
            'berakhir': '2024-06-30',
            'terpakai': 87,
            'kuota': 200,
        },
    ]

    # Simulasi Role Check (Ubah menjadi False untuk melihat tampilan Guest/Customer)
    is_admin = True 

    # Perhitungan Statistik Ringkasan
    stats = {
        'total_promo': len(promosi_list),
        'total_penggunaan': sum(p['terpakai'] for p in promosi_list),
        'total_persentase': len([p for p in promosi_list if p['tipe'] == 'PERSENTASE'])
    }

    context = {
        'promosi': promosi_list,
        'is_admin': is_admin,
        'stats': stats
    }
    
    return render(request, 'admin_promotion_list.html', context)