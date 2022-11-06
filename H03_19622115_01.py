# NIM/Nama  : 19622115/Dahayu Ramaniya Aurasindu
# Tanggal   : 19 Oktober 2022
# Deskripsi : Menghitung diskon terbesar dengan menginput harga barang dan diskon

# Kamus
# jumlahBarang, hrgBarang, diskon = integer

# Algoritma

jumlahBarang = int(input("Masukkan jumlah barang: ")) # Menginput jumlah barang
hrgBarang = [0 for i in range (jumlahBarang)]         # Harga barang awal diinput 0 (selanjutnya akan diubah)
diskon = [0 for i in range (jumlahBarang)]            # diskon awal diinput 0 (selanjutnya akan diubah)

for i in range (jumlahBarang):  
    harga = int(input("Masukkan harga barang ke-" + str(i+1) + ": "))   # Mulai menginput harga barang yang dimasukkan ke array hrgBarang
    hrgBarang[i] = harga

for i in range (jumlahBarang):
    discount = int(input("Masukkan besar diskon barang ke-" + str(i+1) + ": ")) # Mulai menginput diskon yang dimasukkan ke array diskon
    diskon[i] = discount

biggest_sale = 0    # Diskon terbesar awal dimulai dari 0
barang_mana = 0     # barang yang memiliki diskon terbesar
harga_akhir = 0

for i in range (jumlahBarang):
    if ((diskon[i])/100)*hrgBarang[i] > biggest_sale:   # Looping apabila diskon yang dimasukkan lebih besar dari biggest_sale
        i += 1
        diskon_terbesar = diskon[i]
        barang_mana = i
        harga_akhir = hrgBarang[i]
        biggest_sale = (diskon[i]/100)*hrgBarang[i]     # diskon terbesar diubah agar saat looping tidak 0 terus menerus
    
print("Barang " + str(barang_mana + 1) + " memiliki diskon terbesar yaitu " + str(biggest_sale))