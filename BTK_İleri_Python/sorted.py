'''
sayilar = [1,25,36,66,52,24,3]

sonuc = sorted(sayilar, reverse=True)       #reverse tersten sıralar

print(sonuc)

'''

users = [
    {"username": "aliyilmaz","posts":["post1","post2"]},
    {"username": "senilmaz","posts":[""]},
    {"username": "kenanca","posts":["post1","post2","post3"]},
    {"username": "zahidem","posts":["post1"]}
]

sonuc = sorted(users, key=len, reverse = True)
sonuc1 = sorted(users, key=lambda i: i["username"])

sonuc1 = list(map(lambda u: u["username"],sonuc1))  #sonucları sadece username olarak gösterr (***MAP İLE***)

print(sonuc1)