
import unittest
from Activities import eat, nap, is_funny, laugh

class Test(unittest.TestCase):

    def test_eat_healty(self):
        """ Positive message for healty eating """
        self.assertEqual(
            eat("broccoli", is_healty=True),
            "I'm eating broccoli, because it is healty")
        
    def test_eat_healty_boolean(self):
        """ is_healty must be boolean value """
        with self.assertRaises(ValueError):
            eat("pizza", is_healty="who cares?")
        
    def test_eat_unhealty(self): 
        """ Message fo eating unhealty """        
        self.assertEqual(
            eat("pizza", is_healty=False),
            "I'm eating pizza, because it is good")
        
    def test_short_nap(self):
        """ Short naps hould give energy """
        self.assertEqual(
            nap(1),
            "After 1 hour nap I am full of energy!")
        
    def test_long_nap(self):
        """ Long naps are bad """
        self.assertEqual(
            nap(3),
            "I overslept! I didn't mean to nap 3 hours")
        
    def test_is_funny_tim(self):
        self.assertEqual(is_funny("Tim"), False)
        #self.assertEqual(is_funny("Tim"), "Tim should not be funny")
        
    def test_is_funny_anyone_else(self):
        self.assertTrue(is_funny("Sven"), "Sven should be funny")
        self.assertTrue(is_funny("Tammy"), "Tammy should be funny")
        
    def test_laugh(self):
        self.assertIn(laugh(), ("lol", "haha", "tehehe"))
       


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()