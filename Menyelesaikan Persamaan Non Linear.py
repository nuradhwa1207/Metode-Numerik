import numpy as np

# Fungsi yang akan dicari akarnya: f(x) = x + e^x
def f(x):
    return x + np.exp(x)

# 1. Metode Tabel
def metode_tabel(a, b, n):
    """
    Metode Tabel untuk mendekati akar persamaan.
    
    Parameter:
    a : float : Batas bawah dari interval
    b : float : Batas atas dari interval
    n : int   : Jumlah titik dalam interval
    
    Fungsi ini akan membagi interval [a, b] menjadi n bagian,
    dan kemudian menampilkan nilai fungsi di setiap titik tersebut.
    """
    print("Metode Tabel:")
    # Membagi interval menjadi n bagian
    x_values = np.linspace(a, b, n)
    for x in x_values:
        print(f"x = {x:.4f}, f(x) = {f(x):.4f}")
    print()

# 2. Metode Biseksi
def metode_biseksi(a, b, tol, max_iter):
    """
    Metode Biseksi untuk menemukan akar persamaan.
    
    Parameter:
    a : float    : Batas bawah dari interval
    b : float    : Batas atas dari interval
    tol : float  : Toleransi kesalahan yang diinginkan
    max_iter : int : Jumlah iterasi maksimal
    
    Fungsi ini akan mempersempit interval yang mengandung akar
    dengan membagi interval menjadi dua bagian dan memilih
    subinterval yang tetap mengandung akar.
    """
    print("Metode Biseksi:")
    iterasi = 0
    while iterasi < max_iter:
        # Menentukan titik tengah
        c = (a + b) / 2
        # Jika nilai fungsi di titik tengah sudah mendekati nol (sesuai toleransi), maka akar ditemukan
        if abs(f(c)) < tol:
            return c
        # Mempersempit interval berdasarkan tanda f(c)
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iterasi += 1
        print(f"Iterasi {iterasi}: c = {c:.6f}, f(c) = {f(c):.6f}")
    return c

# 3. Metode Regula Falsi
def metode_regula_falsi(a, b, tol, max_iter):
    """
    Metode Regula Falsi untuk menemukan akar persamaan.
    
    Parameter:
    a : float    : Batas bawah dari interval
    b : float    : Batas atas dari interval
    tol : float  : Toleransi kesalahan yang diinginkan
    max_iter : int : Jumlah iterasi maksimal
    
    Metode ini menggunakan pendekatan garis lurus antara dua titik untuk
    memperkirakan di mana akar berada, dan mempersempit interval
    berdasarkan perkiraan tersebut.
    """
    print("Metode Regula Falsi:")
    iterasi = 0
    while iterasi < max_iter:
        # Menentukan titik perkiraan akar berdasarkan Regula Falsi
        c = b - (f(b) * (b - a)) / (f(b) - f(a))
        # Jika nilai fungsi di titik tersebut sudah mendekati nol, maka akar ditemukan
        if abs(f(c)) < tol:
            return c
        # Mempersempit interval berdasarkan tanda f(c)
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iterasi += 1
        print(f"Iterasi {iterasi}: c = {c:.6f}, f(c) = {f(c):.6f}")
    return c

# Parameter-parameter untuk mencari akar
a = -1  # Batas bawah interval
b = 0   # Batas atas interval
tol = 1e-6  # Toleransi kesalahan
max_iter = 50  # Jumlah iterasi maksimal

# 1. Penyelesaian dengan Metode Tabel
n = 10  # Jumlah titik pada metode tabel
print("Penyelesaian Persamaan x + e^x = 0\n")
metode_tabel(a, b, n)

# 2. Penyelesaian dengan Metode Biseksi
akar_biseksi = metode_biseksi(a, b, tol, max_iter)
print(f"\nAkar dengan Metode Biseksi: {akar_biseksi:.6f}")

# 3. Penyelesaian dengan Metode Regula Falsi
akar_regula_falsi = metode_regula_falsi(a, b, tol, max_iter)
print(f"\nAkar dengan Metode Regula Falsi: {akar_regula_falsi:.6f}")
