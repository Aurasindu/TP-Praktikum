# NIM/NAMA  : 19622115/DAHAYU RAMANIYA AURASINDU
# Tanggal   : 15 September 2022
# Deskripsi : Problem 1, program untuk menghitung keuntungan terbesar

# Kamus: 
# hargadasar_a, hargadasar_b, hargadasar_c = int
# hargajual_a, hargajual_b, hargajual_c = int
# keuntungan_a, keuntungan_b, keuntungan_c = int

# Mulai
# Algoritma
hargadasar_a = int(input("Masukkan harga dasar barang A: "))    # Input harga dasar barang A
hargajual_a = int(input("Masukkan harga jual barang A: "))      # Input harga jual barang A
keuntungan_a = hargajual_a-hargadasar_a                         # Menghitung keuntungan penjualan barang A

hargadasar_b = int(input("Masukkan harga dasar barang B: "))    # Input harga dasar barang B
hargajual_b = int(input("Masukkan harga jual barang B: "))      # Input harga jual barang B
keuntungan_b = hargajual_b-hargadasar_b                         # Menghitung keuntungan penjualan barang B

hargadasar_c = int(input("Masukkan harga dasar barang C: "))    # Input harga dasar barang C
hargajual_c = int(input("Masukkan harga jual barang C: "))      # Input harga jual barang C
keuntungan_c = hargajual_c-hargadasar_c                         # Menghitung keuntungan penjualan barang C          

if(keuntungan_a>keuntungan_b and keuntungan_a>keuntungan_c):
# Untuk mengecek apakah keuntungan penjualan barang A adalah yang paling besar.
    print("Barang yang harus ditawarkan adalah barang A")
    # Output menunjukkan bahwa barang A memiliki keuntungan terbesar sehingga harus ditawarkan
elif(keuntungan_b>keuntungan_a and keuntungan_b>keuntungan_c):
    print("Barang yang harus ditawarkan adalah barang B")
    # Output menunjukkan bahwa barang B memiliki keuntungan terbesar sehingga harus ditawarkan
else:
    print("Barang yang harus ditawarkan adalah barang C")
    # Output menunjukkan bahwa barang C memiliki keuntungan terbesar sehingga harus ditawarkan

# Selesai