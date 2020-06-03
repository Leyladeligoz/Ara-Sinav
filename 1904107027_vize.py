#Soru-Algoritma1 Farklı sayılar üretme
# import random
# for i in range(6):
#  dizi=(1,50)
#  for i in dizi:
#   l = random.randint(1, 50)
#  print("üretilen sayı:",l)
        #İkinci Yol
# L=range(1,50)
# print(random.sample(L,6))

# #Soru-Algoritma3 Anonim ve Gömülü Fonksiyonlar
# import functools
# soyad = ['Aygun','Cicek','Deniz','Atar','Dener','Yilmaz']
# toplam_satis_miktari = [['Ayse',3,6,7],['Ece',5,2,4],['Arya',6,5],['Ali',3],['Can',5,7,9,11],['Aybar',2,3]]
# fonk = lambda list1,list2,list3: str(list1) + " " + str(list2) + " " + str(list3)
# topla = lambda sayi1,sayi2: sayi1 + sayi2
# len = []
# malzeme_toplamı = []
# for i in toplam_satis_miktari:
#   len.append(i[0])
# for e in toplam_satis_miktari:
#   toplam = functools.reduce(topla,e[1:])
#   malzeme_toplamı.append(toplam)
# y = map(fonk,len,soyad,malzeme_toplamı)
# print(list(y))

# #Soru-Algoritma2 Dosyaya yazma işlemi
l =int(input("En fazla iki basamaklı olacak şekilde sayı giriniz."))
f = open("Deneme_vize1.txt", "w")
sayı =0
if len(str(y)) ==2:
    while sayı + 1<= y:
        sayı += 1
        a = sayı //10
        l = sayı%10
        if (a + l) % 2 == 0:
         print(sayı, "=", a + l,"Sayı çifttir. Dosyaya yazılamaz.")
        else:
         print(sayı, "=", a + l, "Sayı tektir. Dosyaya yazılabilir.")
         f.write(str(sayı))
         f.write(" - Sayı tektir.Dosyaya yazılabilir."+'\n')
else:
  print("En fazla iki basamaklı sayı girmelisin.")













