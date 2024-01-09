
class Cake:
    toppings=[]
    def __init__(self) -> None:
        self.toppings=[]
    def getName(self):
      return self.name + self.gettoppingsSeparator()
        
    def gettoppingsSeparator(self):
        toppingtowrite =""
        if self.toppings.__len__()>0:
          toppingtowrite= " with "+ " and ".join(self.toppings)
        return toppingtowrite
              

    def getPrice(self):
        return str(self.price) + "$"
    
class Cupcake(Cake):
    name = "🧁"
    price = 1
    def __init__(self) -> None:
        super().__init__()

class Cookie(Cake):
    name = "🍪"
    price = 2
    def __init__(self) -> None:
        super().__init__()

def Chocolate(cake):
    cake.toppings.append("🍫")
    cake.price += 0.15
    return cake

def Nuts(cake):
    cake.toppings.append("🥜")
    cake.price += 0.2
    return cake

