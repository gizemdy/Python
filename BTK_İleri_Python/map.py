'''
#map sadece hafızada yer açıyor, list ekrana listeliyor


sayilar = [1,5,6,3,9]
sayilar_str = ["1","52","23"]
def kareAl(n):
    return n**2

sonuc = list(map(kareAl, sayilar))
print(sonuc)


#en etkili kullanımı
sonuc1 = list(map(lambda sayi:sayi*3, sayilar))
sonuc2 = list(map(int, sayilar_str))        #str inte çevriliyor
print(sonuc1)
print(sonuc2)
'''

# ******sozlukten veri al düzenle*****
kullanicilar = [
    {"ad":"ali", "soyad":"yılmaz"},
    {"ad":"fatma", "soyad":"gorgun"}
]
kullanici = list(map(lambda kisi: kisi["ad"],kullanicilar))
print(kullanici)