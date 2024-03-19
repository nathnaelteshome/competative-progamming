import unittest

class Product:
    def __init__ (self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity cannot be negative")
    
    def calculateTotal(self):
        return self.price * self.quantity
    
class ShoppingCart:
    def __init__(self):
        self.cart = []
    
    def addProduct(self, product):
        self.cart.append(product)

    def getCartTotal(self):
        total = 0
        for item in self.cart:
                total += item.calculateTotal()
        return total



class ProductTest(unittest.TestCase):
    def test_calculate_total(self):
        with self.assertRaises(ValueError):
            product = Product("shoeA", 10, -77)
    
    def test_calculate_total_2(self):
        product = Product("clothA", 10, 10)

        self.assertEqual(product.calculateTotal(), 100)

class TestShoppingCart(unittest.TestCase):
    def test_getcart_total(self):
        cart = ShoppingCart()
        product = Product("clothA", 10, 10)
        cart.addProduct(product)
        self.assertEqual(cart.getCartTotal(), 100)

    def test_getcart_total(self):
        cart = ShoppingCart()
        with self.assertRaises(ValueError):
            product = Product("shoeA", 10, -77)
        # cart.addProduct(product)
        # self.assertEqual(cart.getCartTotal(), 100)

    def test_getcart_empty_cart(self):
        cart = ShoppingCart()
        self.assertEqual(cart.getCartTotal(), 0)

if __name__  == "__main__":
    unittest.main()