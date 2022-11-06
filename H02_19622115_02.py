# NIM/Nama  : 19622115/Dahayu Ramaniya Aurasindu
# Tanggal   : 5 Oktober 2022
# Deskripsi : Menentukan Penjumlahan Bilangan yang Membesar
# Dimana program akan berhenti apabila input mengecil sebanyak 3 kali berturut-turut

# Kamus
# angka2, angka1 = integer

# Algoritma
three = -1
angka1 = -1
i = 1
jumlah = 0

while three < 3:    # Kondisi bilangan mengecil tidak akan sampai 3 kali
    angka2 = int(input("Masukkan angka ke-"+str(i)+": "))
    if angka1 < angka2:         # Saat angka sebelumnya lebih kecil,
        three = 0               # kondisi mengecil tetap, yaitu 0
        if i > 1:               # Dari kondisi yg sebelumnya, dicek lagi apabila sudah memasuki angka kedua dst,
            jumlah += angka2    # akan terus ditambahkan dengan angka selanjutya selama kondisi memenuhi
    elif angka1 >= angka2:      # Namun apabila angka sebelum dan sesudahnya sama atau bahkan angka sebelumnya lebih kecil,
        three += 1              # Maka kondisi mengecil, dan perhitungan akan berhenti saat 'three' mencapai 3
    i += 1
    

print("Jumlah nilai yang membesar adalah", jumlah)