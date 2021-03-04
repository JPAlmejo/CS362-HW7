import unittest
import FizzBuzz

class TestCaseFizzBuzz(unittest.TestCase):
#tests if fizzbuzz even runs at all
    def test1(self):
        self.assertEqual(FizzBuzz.fizzbuzz(5), "1, 2, fizz, 4, buzz")

if __name__== '__main__':
    unittest.main(verbosity=2)