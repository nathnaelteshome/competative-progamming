import unittest

from your_module import Product

class ProductTest(unittest.TestCase):
    def test_calculate_total(self):
        # Create an instance of the Product class
        product = Product("Example Product", 10, 5)

        # Call the calculateTotal method and assert the expected result
        self.assertEqual(product.calculateTotal(), 50)

if __name__ == '__main__':
    unittest.main()