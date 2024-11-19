import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()
        
    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
        
    def test_teen_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(15), 100)
        
    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(30), 150)
        
    def test_senior_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(65), 100)
        
    def test_infant_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(0), None)
        
    def test_negative_age_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-5), None)
        
    def test_edge_case_12_years_old(self):
        self.assertEqual(self.zoo.get_ticket_price(12), 50)
        
    def test_edge_case_13_years_old(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)
    
    def test_edge_case_20_years_old(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)
    
    def test_edge_case_21_years_old(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)
    
    def test_edge_case_60_years_old(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 100)

if __name__ == '__main__':
    unittest.main()

    # Add your additional test cases here.