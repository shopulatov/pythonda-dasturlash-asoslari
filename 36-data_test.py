import unittest
from kattasi import kattasini_top

class MaxTest(unittest.TestCase):
    def kattasini_top_test(self):
        self.assertEqual(kattasini_top(20,19,25), 25)
        self.assertEqual(kattasini_top(0,-19,2), 2)
        self.assertEqual(kattasini_top(-20,1,5), 25)
        
unittest.main()
