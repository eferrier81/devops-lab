# test_app.py 
import unittest 
from app import calculate_tax 
 
class TestTaxCalculator(unittest.TestCase): 
 
    def test_zero_tax_bracket(self): 
        self.assertEqual(calculate_tax(100000), 0) 
        self.assertEqual(calculate_tax(150000), 0) 
 
    def test_five_percent_bracket(self): 
        self.assertEqual(calculate_tax(250000), 5000) 
 
    def test_ten_percent_bracket(self): 
        self.assertEqual(calculate_tax(400000), 17500) 
 
    def test_fifteen_percent_bracket(self): 
        self.assertEqual(calculate_tax(600000), 42500) 
 
    def test_twenty_percent_bracket(self): 
        self.assertEqual(calculate_tax(1000000), 115000) 
 
    def test_negative_income(self): 
        # Should this return 0 or raise an error? 
        # Discuss: What is the expected behavior? 
        pass 
 
if __name__ == "__main__": 
    unittest.main()