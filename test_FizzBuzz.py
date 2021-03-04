import unittest
import FizzBuzz

class TestCaseFizzBuzz(unittest.TestCase):
#tests if fizzbuzz even runs at all
    def test1(self):
        self.assertEqual(FizzBuzz.FizzBuzz(100))

if __name__== '__main__':
    unittest.main(verbosity=2)