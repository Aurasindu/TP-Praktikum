# NIM/NAMA  : 19622115/DAHAYU RAMANIYA AURASINDU
# Tanggal   : 15 September 2022
# Deskripsi : Problem 2, mengelompokkan kelas berdasarkan NIM

# Kamus:
# NIM = int

# Mulai
# Algoritma
NIM = (int(input("Masukkan 3 digit terakhir NIM Anda:")))   # Memasukkan 3 digit terakhir NIM Mahasiswa

if(NIM%2==0 and 1<=NIM<=100):               # Mengecek 3 digit terakhir NIM genap dengan rentang 1 sampai dengan 100
    print("Mahasiswa masuk ke kelas K2")    
    # Output menunjukkan bahwa mahasiswa masuk ke kelas K2
elif(NIM%2==1 and 1<=NIM<=100):             # Mengecek 3 digit terakhir NIM ganjil dengan rentang 1 sampai dengan 100
    print("Mahasiswa masuk ke kelas K1")
    # Output menunjukkan bahwa mahasiswa masuk ke kelas K1
elif(NIM%2==0 and 101<=NIM<=200):           # Mengecek 3 digit terakhir NIM genap dengan rentang 101 sampai dengan 200
    print("Mahasiswa masuk ke kelas K4")
    # Output menunjukkan bahwa mahasiswa masuk ke kelas K4
elif(NIM%2==1 and 101<=NIM<=200):           # Mengecek 3 digit terakhir NIM ganjil dengan rentang 101 sampai dengan 200
    print("Mahasiswa masuk ke kelas K3")
    # Output menunjukkan bahwa mahasiswa masuk ke kelas K3
elif(NIM%2==0 and 201<=NIM<=300):           # Mengecek 3 digit terakhir NIM genap dengan rentang 201 sampai dengan 300
    print("Mahasiswa masuk ke kelas K6")
    # Output menunjukkan bahwa mahasiswa masuk ke kelas K6
elif(NIM%2==1 and 201<=NIM<=300):           # Mengecek 3 digit terakhir NIM ganjil dengan rentang 1 sampai dengan 100
    print("Mahasiswa masuk ke kelas K5")
    # Output menunjukkan bahwa mahasiswa masuk ke kelas K5
elif(NIM%2==0 and NIM>300):                 # Mengecek 3 digit terakhir NIM genap dengan rentang angka > 300
    print("Mahasiswa masuk ke kelas K8")
    # Output menunjukkan bahwa mahasiswa masuk ke kelas K8
elif(NIM%2==1 and NIM>300):                 # Mengecek 3 digit terakhir NIM ganjil dengan rentang angka > 300
    print("Mahasiswa masuk ke kelas K7")
    # Output menunjukkan bahwa mahasiswa masuk ke kelas K7

# Selesai