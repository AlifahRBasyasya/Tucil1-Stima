# Nama      : Alifah Rahmatika Basyasya
# NIM       : 13519053
# Tanggal   : 27 Januari 2021
# Deskripsi : Cryptarithmetic - Brute Force (Tucil1 Stima)

import time

def BacaFile(namafile):
    #Membaca file dan menyimpannya dalam matriks. Menyimpan inisial, mengecek jumlah huruf
    #KAMUS LOKAL
    #i: integer
    global Maks
    global Matriks
    global Inisial
    global JmlHuruf
    global ArrayHuruf
    #ALGORITMA
    file = open("../test/" + namafile, "r")
    teks = file.readline().strip(" \n")
    while (teks != ""):
        if (teks[0] != "-") and (teks[0] != "+"):
            if (teks[0] not in Inisial):
                Inisial.append(teks[0])
            idx = 9
            huruf = ["" for i in range(10)]
            for i in range(len(teks)-1, -1, -1):
                huruf[idx] = teks[i]
                idx -= 1
                if (teks[i] not in ArrayHuruf[0]):
                    if (JmlHuruf < 10):
                        ArrayHuruf[0].append(teks[i])
                        JmlHuruf += 1
                    else:
                        print("Error. Maksimal terdapat 10 huruf berbeda")
                        Maks = True
            Matriks.append(huruf)
        teks = file.readline().strip(" +\n")
    file.close()

def KonversiKar(Kar, ArrayHuruf, Array):
    #Mengubah karakter menjadi angka sesuai jawaban
    #KAMUS LOKAL
    #i: integer
    #ALGORITMA
    i = 0
    if Kar == "" or Kar == " ":
        return 0
    else:
        i = 0
        while i < len(ArrayHuruf[0]) and Kar != ArrayHuruf[0][i]:
            i += 1
        return Array[i]

def Cek(Matriks, ArrayHuruf, Inisial, Array):
    #Mengecek kebenaran jawaban
    #KAMUS LOKAL
    #Baris, Total, i, j, c: integer
    #Benar: boolean
    #ALGORITMA
    Baris = len(Matriks)-1
    Total = 0
    i = 9
    Benar = True
    for c in Inisial:
        if (KonversiKar(c, ArrayHuruf, Array) == 0):
            Benar = False
    while (i >= 0) and (Benar):
        for j in range(Baris):
            Total += KonversiKar(Matriks[j][i], ArrayHuruf, Array)
        if (Total%10 != KonversiKar(Matriks[Baris][i], ArrayHuruf, Array)):
            Benar = False
        else:
            Total = Total//10
            i -= 1
    return Benar

def Permutasi(JmlHuruf, Jawab, Inisial, Matriks):
    #Mencari kemungkinan kombinasi angka pada jumlah huruf kemudian mengecek kebenaran
    #KAMUS LOKAL
    #i, j, idx: integer
    global Found
    global Count
    global ArrayHuruf
    #ALGORITMA
    if (not Found):
        if (JmlHuruf==0):
            Count += 1
            if (Cek(Matriks, ArrayHuruf, Inisial, Jawab)):
                Found = True
                for j in range(len(ArrayHuruf[0])):
                    ArrayHuruf[1][j] = Jawab[j]
        else:
            i = 0
            while (not Found) and (i < 10):
                idx = len(Jawab)-JmlHuruf
                if (i not in Jawab) and ((i!=0) or (ArrayHuruf[0][idx] not in Inisial)):
                    Jawab[idx] = i
                    Permutasi(JmlHuruf-1, Jawab, Inisial, Matriks)
                if (not Found):
                    i += 1
                Jawab[idx] = -1
    

def PrintSoal(Matriks, ArrayHuruf):
    #KAMUS LOKAL
    #i, j, k: integer
    #ALGORITMA
    Baris = len(Matriks)-1
    for i in range(Baris):
        print()
        for j in range(10):
            if (Matriks[i][j] != ""):
                print(Matriks[i][j], end="")
            else:
                print(" ", end="")
    print("+\n"+10*"-")
    for k in range(10):
        if (Matriks[Baris][k] != ""):
            print(Matriks[Baris][k], end="")
        else:
            print(" ", end="")
    print("\n")
        
def PrintJawaban(Matriks, ArrayHuruf):
    #KAMUS LOKAL
    #i, j, k: integer
    #ALGORITMA
    print("Solusi:")
    Baris = len(Matriks)-1
    for i in range(Baris):
        print()
        for j in range(10):
            if (Matriks[i][j] == " ") or (Matriks[i][j] == ""):
                print(" ", end="")
            else:
                print(KonversiKar(Matriks[i][j], ArrayHuruf, ArrayHuruf[1]), end="")
    print("+\n"+10*"-")
    for k in range(10):
        if (Matriks[Baris][k] != ""):
            print(KonversiKar(Matriks[Baris][k], ArrayHuruf, ArrayHuruf[1]), end="")
        else:
            print(" ", end="")
    print("\n")

#MAIN PROGRAM
#KAMUS
#ALGORITMA
Maks = False
Matriks = []
Inisial = []
ArrayHuruf = [[],[0 for i in range(10)]]
JmlHuruf = 0
Count = 0
Found = False
#Input nama file
namafile = input("Masukkan nama file beserta .txt: ")

#Membaca file
BacaFile(namafile)

if (not Maks):
    #Menyimpan waktu awal
    mulai = time.time()

    #Mencari solusi
    Jawab = [-1 for i in range(JmlHuruf)]
    Permutasi(JmlHuruf, Jawab, Inisial, Matriks)

    #Menampilkan hasil
    if (Found):
        PrintSoal(Matriks, ArrayHuruf)
        PrintJawaban(Matriks, ArrayHuruf)
    else:
        print("Tidak memiliki solusi\n")
    print("Solusi ditemukan pada percobaan ke-" + str(Count))
    print("Waktu yang dibutuhkan yaitu", time.time()-mulai)
