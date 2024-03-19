import unittest

class Product:
    def __init__ (self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def  calculateTotal(self):
        return self.price * self.quantity


class ProductTest(unittest.TestCase):
    def test_calculate_total(self):
        product = Product("shsoe", 10, -77)

        self.assertRaises(ValueError, product.calculateTotal)
    
    def test_calculate_total_2(self):
        product = Product("clotha", 10, 10)

        self.assertEqual(product.calculateTotal(), 100)

if __name__  == "__main__":
    unittest.main()