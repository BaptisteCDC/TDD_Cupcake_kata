class Cake:
    base=""
    topping=[]
    price: float=0
    def __init__(self,base,price) -> None:
        self.base = base
        self.topping=[]
        self.price=price
    def printName(self):
        toppingtowrite =""
        if self.topping.__len__()>0:
          toppingtowrite= " with "+ " and ".join(self.topping)
        return self.base + toppingtowrite
    def printPrice(self):
        return str(round(self.price,2))+"$"
    
class Cupcake(Cake):
    def __init__(self) -> None:
        super().__init__("🧁",1)


class Cookie(Cake):
    def __init__(self) -> None:
        super().__init__("🍪",2)



def Chocolate(cake:Cake) -> Cake:
    cake.topping.append("🍫")
    cake.price= cake.price + 0.1
    return cake

def Nuts(cake:Cake) -> Cake:
    cake.topping.append("🥜")
    cake.price+=0.2
    return cake

def sugar(cake:Cake) -> Cake:
    cake.topping.append("🍬")
    cake.price+=0.15
    return cake


    

