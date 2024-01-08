from pastery import *

def test_cupcake_name_return_cake_draw():
    assert Cupcake().printName() == "🧁"

def test_cupcake_price_return_cake_price():
    assert Cupcake().printPrice() == "1$"

def test_cookie_name_return_cookie_draw():
    gateau = Cookie()
    assert gateau.printName()  == "🍪"

def test_cookie_price_return_cookie_price():
    gateau = Cookie()
    assert gateau.printPrice()  == "2$"

def test_cookie_with_chocolote_name_return_cookie_chocolate_draw():
    gateau = Chocolate(Cookie())
    assert gateau.printName()  == "🍪 with 🍫"

def test_cookie_with_chocolote_price_return_cookie_chocolate_price():
    gateau = Chocolate(Cookie())
    assert gateau.printPrice()  == "2.1$"

def test_cupcake_with_chocolote_name_return_cupcake_chocolate_draw():
    gateau = Chocolate(Cupcake())
    assert gateau.printName()  == "🧁 with 🍫"

def test_cupcake_with_chocolote_price_return_cupcake_chocolate_price():
    gateau = Chocolate(Cupcake())
    assert gateau.printPrice()  == "1.1$"

def test_cupcake_with_chocolote2_name_return_cupcake_chocolate2_draw():
    gateau = Chocolate(Chocolate(Cupcake()))
    assert gateau.printName()  == "🧁 with 🍫 and 🍫"

def test_cupcake_with_chocolote2_price_return_cupcake_chocolate2_price():
    gateau = Chocolate(Chocolate(Cupcake()))
    assert gateau.printPrice()  == "1.2$"


def test_cupcake_with_chocolote_and_nuts_name_return_cupcake_chocolate_nuts_draw():
    gateau = Nuts(Chocolate(Cupcake()))
    assert gateau.printName()  == "🧁 with 🍫 and 🥜"

def test_cupcake_with_chocolote_and_nuts_pricereturn_cupcake_chocolate_nuts_price():
    gateau = Nuts(Chocolate(Cupcake()))
    assert gateau.printPrice()  == "1.3$"

def test_cupcake_with_chocolote_and_nuts2_name_return_cupcake_chocolate_nuts_draw():
    gateau = Nuts(Nuts(Chocolate(Cupcake())))
    assert gateau.printName()  == "🧁 with 🍫 and 🥜 and 🥜"

def test_cupcake_with_chocolote_and_nuts2_price_return_cupcake_chocolate_nuts_price():
    gateau = Nuts(Nuts(Chocolate(Cupcake())))
    assert gateau.printPrice()  == "1.5$"



def test_cupcake_with_chocolote_and_sugar_name_return_cupcake_chocolate_sugar_draw():
    gateau = sugar(Chocolate(Cupcake()))
    assert gateau.printName()  == "🧁 with 🍫 and 🍬"


def test_cupcake_with_csugar_and_chocolate_name_return_cupcake_chocolate_sugar_draw():
    gateau = Chocolate(sugar(Cupcake()))
    assert gateau.printName()  == "🧁 with 🍬 and 🍫"

def test_cupcake_with_chocolote_and_sugar_price_return_cupcake_chocolate_sugar_price():
    gateau = sugar(Chocolate(Cupcake()))
    assert gateau.printPrice()  == "1.25$"

    

