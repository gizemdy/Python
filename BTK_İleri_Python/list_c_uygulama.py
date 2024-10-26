'''
-1. 1-100 arasındaki sayılardan 12e tam bolunebilenleri bulunuz
-2. verilen text içerisindeki rakamları içeren bir text oluştur
    text = "hello 123546 world" --> [1,2,3,5,4,6]
-3. sıcaklıklara göre 4 derecenin altındaki sıcaklıklara buzlanma tehlikesi yaz
    sicakliklar = [20,15,0,-5,-2]
-4. Ogrenciler ve notlar ekrana dict verisi seklinde yazsın
ogr = ["ali", "ahmet", "canan"]
notlar = [50,60,80]

#1

sayilar = [sayi for sayi in range(1,101) if sayi%3 == 0 | sayi%4 == 0 ] #else kullanımı olmadığı için ifi sona yazıoruz. 
#bu şekilde int şeklinde yazıyor, başa yazdığımızda true false yazıyor
print(sayilar)

#2
text = "hello 123546 world"
yazi = [item for item in text if item.isdigit()]
print(yazi)

#3 IF-ELSE ILE YAPILIYOR
sicakliklar = [20,15,0,-5,-2]
buzlanma = [item if item >4 else "buzlanma tehlikesi" for item in sicakliklar]
print(buzlanma)

#4 DICT YONTEMI (SOZLUK)
ogr = ["ali", "ahmet", "canan"]
notlar = [50,60,80]
liste = [(ogr[i],notlar[i]) for i in range(0,len(ogr))]
print(liste)

listee = { key:value for (key, value) in liste if value >50 }
print(listee) 

'''
#5

sonuc = [(x,y) for x in range(3) for y in range(3)]
print(sonuc)