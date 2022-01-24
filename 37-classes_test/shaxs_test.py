import unittest
from shaxs import Shaxs,Talaba

class ShaxsTest (unittest.TestCase):
    def setUp(self):
        ism = "Ali"
        familya = "Hasanov"
        passport = "AC1809809"
        tyil = 1999
        self.shaxs1 = Shaxs(ism,familya,passport,tyil)
        
    def test_create(self):
        self.assertIsNotNone(self.shaxs1.ism)
        self.assertIsNotNone(self.shaxs1.familya)
        self.assertIsNotNone(self.shaxs1.passport)
        self.assertIsNotNone(self.shaxs1.tyil)
        
    def test_get_info(self):
        shaxs1_info = "Ali Hasanov. Passport:AC1809809, 1999-yilda tug`ilgan"
        self.assertEqual(shaxs1_info, self.shaxs1.get_info())
        
    def test_get_age(self):
        shaxs1_age = 23
        self.assertEqual(shaxs1_age, self.shaxs1.get_age(2022))
        
unittest.main()

# class TalabaTest (unittest.TestCase):
#     def setUp(self):
#         ism = "Ali"
#         familya = "Hasanov"
#         passport = "AC1809809"
#         tyil = 1999
#         idraqam = '0000005'
        
#         self.shaxs1 = Talaba(ism,familya,passport,tyil,idraqam)
        
#     def test_create(self):
#         self.assertIsNotNone(self.shaxs1.ism)
#         self.assertIsNotNone(self.shaxs1.familya)
#         self.assertIsNotNone(self.shaxs1.passport)
#         self.assertIsNotNone(self.shaxs1.tyil)
#         self.assertIsNotNone(self.shaxs1.idraqam)
        
# unittest.main()    