# NIM/Nama  : 19622115/Dahayu Ramaniya Aurasindu
# Tanggal   : 5 Oktober 2022
# Deskripsi : Menentukan Bilangan Sempurna

# Kamus
# N = integer

# Algoritma
N = int(input("Masukkan bilangan: "))
jumlah = 0

for i in range(1, N+1):     # Mengecek range mulai dari 1 hingga N
    if N % i == 0:          # Mencari faktor dari N
        jumlah = jumlah + i # Menjumlahkan faktor dari N
if jumlah - N == N:         # Mengecek apakah N termasuk bilangan sempurna
    # Dengan cara jumlah faktor dikurangi N, karena N tidak masuk hitungan
    print("Bilangan tersebut adalah bilangan sempurna") 
else:
    print("Bilangan tersebut bukan bilangan sempurna")
    
