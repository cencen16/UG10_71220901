print ("~~~~~~~~~~~~/('V')\~~~~~~~~~~~~~: ")
print (" PROGRAM PERHITUNGAN VOLUME BANGUN RUANG: ")
print ("~~~~~~~~~~~/('v')\~~~~~~~~~~~~~~: ")

print ("pilih salah satu bangun ruang yang ingin di hitung volumenya: ")
print ("1. Limas: ")
print ("2. Bola: ")
print ("3. Prisma: ")
print ("4. Kerucut: ")
e = int (input("masukkan pilihan anda: "))
if e == 1 :
    ab = int (input ("Masukkan panjang sisi alas limas :"))
    ac = int (input ("Masukkan tinggi limas :"))
    limas = 1/3 * ab * ac
    print ("volume limas tersebut adalah :", limas)
elif e == 2 :
    ba = int (input ("masukkan jari jari bola :"))
    bola = (4/3) * 3.14 * ba
    print ("volume bola tersebut adalah :", bola)
elif e == 4 :
   R = int(input("masukkan jari-jari kerucut"))
   T = int(input("masukkan tinggi kerucut"))
   kerucut = (1/3*(3.14))
   print = int(input("volume kerucut tersebut adalah",kerucut))



