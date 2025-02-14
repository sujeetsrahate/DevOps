import unittest

def add(a,b):
    return a+b

class TestAddFunciton(unittest.TestCase):
    def test_add_positive_number(self):
        self.assertEqual(add(2,3),5,"add 2,3 return some number other than 5")
    def test_add_negative_number(self):
        self.assertEqual(add(-2,-3),-5,"add 2,3 return some number other than -5")
    def test_add_mix_number(self):
        self.assertEqual(add(-2,3),1,"add 2,3 return some number other than 1")
    


if __name__ == '__main__':
    unittest.main()