# NIM/Nama  : 19622115/Dahayu Ramaniya Aurasindu
# Tanggal   : 19 Oktober 2022
# Deskripsi : Menentukan jumlah kemunculan string 1 pada string 2

# Kamus
# string1, string2 = string
# len_string1, len_atring2 = integer

# Algoritma
len_string1 = int(input("Masukkan panjang string 1: ")) # Input jumlah huruf
string1 = input("Masukkan string 1: ")  # Input string pertama
len_string2 = int(input("Masukkan panjang string 2: ")) # Input jumlah huruf string kedua
string2 = input("Masukkan string 2: ")  # Input string kedua

count = 0   # Untuk menghitung jumlah kemunculan string 1
hurufsama = 0   # Untuk menghitung jumlah huruf yang sama dengan string 1 

for i in range (len_string2):   # Looping sebanyak jumlah huruf pada string 2
    if string2[i] == string1[0]:    # Pengecekan pertama apabila ada huruf pada string 2 yang sama dengan huruf pertama string 1
        k = i
        hurufsama = 0
        for j in range (len_string1):   # Looping kedua sebanyak jumlah huruf pada string 1
            if k < len_string2: # Pengecekan pertama agar huruf yang sama tidak melebihi panjang string 2
                if string2[k] == string1[j]:    # Apabila huruf pada string 2 sama dengan string 1 maka variabel hurufsama ditambah
                    hurufsama += 1
            k += 1
        if hurufsama == len_string1:    # Apabila jumlah huruf sama sama dengan panjang string 1, maka jumlah kemunculan string 1 ditambah
            count += 1
print("String 1 muncul sebanyak " + str(count) + " kali.")
