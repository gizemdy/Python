class CartItem:         #nesneleri üret
    #constructor --- yapıcı metod
    def __init__(self,name,price,quantity):
        self.name= name
        self.price=price
        self.quantity = quantity

#instance methods (fonksiyonu tanımlayıp her bir nesne için aynı işlemi yaptırcak)
    def calculate_total(self):
        return self.price*self.quantity

    def discount(self):
        return self.price * 0.4
item1 = CartItem("Telefon", 5000 ,1)

item2 = CartItem("Computer", 15000 ,2)

item3 = CartItem("book", 120, 4)


class ShoppingCart:         #cartitemla üretilen nesneleri bir sepette yönet
    
    def __init__(self, liste):
        self.liste = liste
    def add_item(self, item):
        self.liste.append(item3)
    def display_items(self):
        for i in self.liste:
            print(f"{i.name} {i.price}")
    def calculate_totals(self):
       return sum([item.price*item.quantity for item in self.liste])
    def remove_item(self,cart_item):
        self.liste = [item for item in self.liste if item != cart_item]
    def clear(self):
        self.liste=[]
        
    
# ctrl k c -----> yorum satırı 

# sc = ShoppingCart([item1,item2])
# sc.add_item(item3)
# sc.display_items()
# print(sc.calculate_totals())
# sc.remove_item(item2)
# sc.clear()