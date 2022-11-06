# NIM/Nama  : 19622115/Dahayu Ramaniya Aurasindu
# Tanggal   : 19 Oktober 2022
# Deskripsi : Menentukan kondisi akhir lampu (mati/menyala) apabila tombol yang ditekan
# juga akan mempengaruhi kondisi lampu di sebelahnya

# Kamus
# lamp, tekanTombol, tekanKe, nyala_awal = integer

# Algoritma
lamp = int(input("Masukkan banyak lampu: "))    # Menginput jumlah lampu
tekanTombol = int(input("Masukkan berapa kali Tuan Kil menekan tombol: "))  # Menginput jumlah penekanan tombol oleh user
nyala_awal = [0 for i in range (lamp+2)]    # array untuk mengetahui nyala/mati lampu 
                                            # penginputan +2 karena penekanan tombol berpengaruh terhadap lampu kanan dan kiri
                                            # tetapi yang diprint dimulai dari indeks ke-0 hingga lamp+1

for i in range (1, tekanTombol+1):  # Looping hingga Tuan Kil selesai menekan tombol
    tekanKe = int(input("Tombol yang ditekan ke-" + str(i) + ": "))
    if nyala_awal[tekanKe] == 0:    # Apabila lampu awalnya dalam keadaan mati, maka diubah menjadi nyala
        nyala_awal[tekanKe] = 1     # begitu pula sebaliknya
    else:
        nyala_awal[tekanKe] = 0
    if nyala_awal[tekanKe-1] == 0:  # Ini adalah keadaan lampu di sebelahnya (kiri), sama seperti di atas
        nyala_awal[tekanKe-1] = 1
    else:
        nyala_awal[tekanKe-1] = 0
    if nyala_awal[tekanKe+1] == 0:  # Ini adalah keadaan lampu di sebelahnya (kanan), sama seperti di atas
        nyala_awal[tekanKe+1] = 1
    else:
        nyala_awal[tekanKe+1] = 0
print("Keadaan akhir rangkaian lampu adalah", end=" ")
for i in range (1, lamp+1):     # Looping untuk mem-print keadaan lampu dari indeks pertama hingga lamp+1
    print(nyala_awal[i], end='')
print(".")
    