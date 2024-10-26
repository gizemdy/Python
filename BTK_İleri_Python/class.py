class CartItem:
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


#print(item1.calculate_total())
print(item2.discount())