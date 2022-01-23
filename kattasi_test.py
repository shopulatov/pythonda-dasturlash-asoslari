import unittest
from kattasi import kattalashtir

class KattalashtirishTest(unittest.TestCase):
    def kattalashtir_test(self):
        katta = kattalashtir(['bir', 'ikki', 'uch'])
        self.assertEqual(katta, ['Bir', 'ikki', 'Uch'])

unittest.main()