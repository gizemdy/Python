'''
liste = []
for i in range(0,5):
    liste.append(i)
print(liste)

liste = [item for item in range(5)]
print(liste)
-----------------------
sayilar = []
for i in range(5):
    sayilar.append(i)
print(sayilar)
sayilar = [item*2 for item in range(0,5)]
print(sayilar)
--------------------------
kurum="BTK AKADEMİ"
kurum1 = [item.lower() for item in kurum]
print(kurum1)
----------------------------
#IF ELSE
sayilar = [12,25,36,54,85,62]
kosul=[]
kosul = [item if item>45 else "küçüktür "for item in sayilar]

print(kosul)
---------------------------------

kdv=[]
urun_fyt =[3000,5000,9000,1000,2500,1500,1700]
kdv=[i if i>3000 else "kdv yok" for i in urun_fyt]
print(kdv)
--------------------------------------
'''
