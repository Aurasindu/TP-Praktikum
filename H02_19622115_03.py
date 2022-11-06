# NIM/Nama  : 19622115/Dahayu Ramaniya Aurasindu
# Tanggal   : 5 Oktober 2022
# Deskripsi : Menentukan Bilangan Sempurna

# Kamus
# N = integer

# Algoritma
N = int(input("Masukkan N: "))
isprima = True

print("Faktor primanya adalah", end=" ")

for i in range (1, N+1):    # Dalam rentang 1 hingga N
    if N % i == 0:
        if i < 2:
            isprima = False
        else:
            for j in range (2, i):
                if i % j == 0:
                    isprima = False
        if isprima:
            print(i, end=" ")
        else:
            isprima = True

