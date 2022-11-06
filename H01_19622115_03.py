# NIM/NAMA  : DAHAYU RAMANIYA AURASINDU
# Tanggal   : 15 September 2022
# Deskripsi : Problem 3, menentukan waktu yang dibutuhkan Pak Riz untuk mengelilingi Saraga

# Kamus:
# jam_mulai, menit_mulai, detik_mulai       = int
# jam_selesai, menit_selesai, detik_selesai = int
# jumlah_jam, jumlah_detik, jumlah_menit    = int

# Mulai
# Algoritma
print("Masukkan waktu mulai!")
jam_mulai = int(input("Jam: "))         # Input jam waktu lari dimulai
menit_mulai = int(input("Menit: "))     # Input menit waktu lari dimulai
detik_mulai = int(input("Detik: "))     # Input detik waktu lari dimulai

print("Masukkan waktu selesai!")
jam_selesai = int(input("Jam: "))       # Input jam waktu lari selesai
menit_selesai = int(input("Menit: "))   # Input menit waktu lari selesai
detik_selesai = int(input("Detik: "))   # Input detik waktu lari selesai

jumlah_detik = 0                                 # Mendefinisikan variabel global untuk menyimpan nilai jumlah detik
if(detik_mulai>detik_selesai):                   # Mengecek apabila detik mulai lebih besar dari detik selesai
    jumlah_detik = 60 - detik_mulai                 
    jumlah_detik = jumlah_detik + detik_selesai
elif(detik_mulai<detik_selesai):                 # Mengecek apabila detik mulai lebih kecil dari detik selesai
    jumlah_detik = detik_selesai - detik_mulai

jumlah_menit = 0                                 # Mendefinisikan variabel global untuk menyimpan nilai jumlah menit
if(menit_mulai>menit_selesai):                   # Mengecek apabila menit mulai lebih besar dari menit selesai
    jumlah_menit = 60 - (menit_mulai + 1)
    jumlah_menit = jumlah_menit + menit_selesai
elif(menit_mulai<menit_selesai):                # Mengecek apabila menit mulai lebih kecil dari detik selesai
    jumlah_menit = menit_selesai - menit_mulai

jumlah_jam = 0                                  # Mendefinisikan variabel global untuk menyimpan nilai jumlah jam
if(jam_mulai<jam_selesai):                      # Mengecek apabila jam mulai kurang dari jam selesai, hanya ada 1 kondisi karena jam mulai selalu kurang dari jam selesai
    jumlah_jam = jam_selesai - (jam_mulai + 1)

print("Tuan Riz berlari selama", jumlah_jam, "jam", jumlah_menit, "menit", jumlah_detik, "detik.")

# Selesai