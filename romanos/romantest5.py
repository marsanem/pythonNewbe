import roman5
import unittest

class ToRomanBadInput(unittest.TestCase):
    def test_too_large(self):
        '''to_roman should fail with large input'''
        self.assertRaises(roman5.OutOfRangeError, roman5.to_roman, 4000)
    
    def test_zero(self):
        '''to_roman should fail with 0 input'''
        self.assertRaises(roman5.OutOfRangeError, roman5.to_roman, 0)
    
    def test_negative(self):
        '''to_roman should fail with negative input'''
        self.assertRaises(roman5.OutOfRangeError, roman5.to_roman, -1)

    def test_non_integer(self):
        '''to_roman should fail with non-integer input'''
        self.assertRaises(roman5.NotIntegerError, roman5.to_roman, 0.5)



class RoundtripCheck(unittest.TestCase):
    def test_roundtrip(self):
        '''from_roman(to_roman(n))==n for all n'''
        for integer in range(1, 4000):
            numeral = roman5.to_roman(integer)
            result = roman5.from_roman(numeral)
            self.assertEqual(integer, result)

if __name__ == '__main__':
    unittest.main()