import unittest
import LeapYear

class TestCaseLeapYear(unittest.TestCase):
#tests if year is a leap year
    def test1(self):
        self.assertEqual(LeapYear.leap_year(2000), True)

if __name__== '__main__':
    unittest.main(verbosity=2)