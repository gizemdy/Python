'''
# MAP KULLANIMI
sayilar = [1,5,6,-9,-8,7,-5]
sonuc = list(filter(lambda i: i<0,sayilar)) #fonksiyon tanımlama aşamasını kısalttık , nereye uygulayacağımızı yazdık (sayılar)

sonuc1 = list(filter(lambda i: i%2==1, sayilar))
print(sonuc)
print(sonuc1)


#FILTER VE MAP FARKI

isimler=["çınar","adem", "yazgı", "izzet","bade","derya", "ayse","aysun"]
liste = list(filter(lambda i: i[0]=="a", isimler))
list2 = list(map(lambda i: i.upper(), liste))
#print(liste)
print(list2)

#BİR ÖRNEK

'''
users = [
    {"username": "aliyilmaz","posts":["post1","post2"]},
    {"username": "senilmaz","posts":[""]},
    {"username": "kenanca","posts":["post1","post2","post3"]},
    {"username": "zahidem","posts":["post1"]}
]

bilgiler = list(filter(lambda i: len(i["posts"])>1, users))     #1den fazla post varsa tüm bilgilerini al
bilgi = list(map(lambda i: i["username"],bilgiler))     #1den fazla postu olanların username yazdır
print(bilgi)