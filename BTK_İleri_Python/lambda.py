#LAMBDA FONKSİYON İŞLEMLER

def kareal(a):
    return a**2
sonuc = kareal(5)

sonuc = (lambda a:a ** 2)(3)
print(sonuc)

toplama = lambda a,b,c: a+b + c
sonuc=toplama(1,6,5)
print(sonuc)

def myFunc(n):
    return lambda a:a*n
