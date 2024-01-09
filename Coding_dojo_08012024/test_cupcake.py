from bakery import *

def test_it_should_return_cupcake():
  cake = Cupcake()
  assert cake is not None

def test_it_should_return_cupcake_name():
  cake = Cupcake()
  assert cake.getName() == "🧁"

def test_it_should_return_cupcake_price():
  cake = Cupcake()
  assert cake.getPrice() == "1$"

def test_it_should_return_cookie():
  cake = Cookie()
  assert cake is not None

def test_it_should_return_cookie_name():
  cake = Cookie()
  assert cake.getName() == "🍪"  

def test_it_should_return_cookie_price():
  cake = Cookie()
  assert cake.getPrice() == "2$"

def test_it_should_return_cookie_with_chocolate():
  cake = Chocolate(Cookie())
  assert cake.getName() == "🍪 with 🍫"

def test_it_should_return_cupcake_with_chocolate():
  cake = Chocolate(Cupcake())
  assert cake.getName() == "🧁 with 🍫"

def test_it_should_return_cookie_with_chocolate():
  cake = Chocolate(Cookie())
  assert cake.getPrice() == "2.15$"

def test_it_should_return_cupcake_with_chocolat_price():
  cake = Chocolate(Cupcake())
  assert cake.getPrice() == "1.15$"

def test_it_should_return_cookie_with_nuts():
  cake = Nuts(Cookie())
  assert cake.getName() == "🍪 with 🥜"

def test_it_should_return_cookie_with_chocolate_and_nuts():
  cake = Nuts(Chocolate(Cookie()))
  assert cake.getName() == "🍪 with 🍫 and 🥜"
