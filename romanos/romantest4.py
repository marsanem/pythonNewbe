import roman4
import unittest

class ToRomanBadInput(unittest.TestCase):
    def test_too_large(self):
        '''to_roman should fail with large input'''
        self.assertRaises(roman4.OutOfRangeError, roman4.to_roman, 4000)
    
    def test_zero(self):
        '''to_roman should fail with 0 input'''
        self.assertRaises(roman4.OutOfRangeError, roman4.to_roman, 0)
    
    def test_negative(self):
        '''to_roman should fail with negative input'''
        self.assertRaises(roman4.OutOfRangeError, roman4.to_roman, -1)

    def test_non_integer(self):
        '''to_roman should fail with non-integer input'''
        self.assertRaises(roman4.NotIntegerError, roman4.to_roman, 0.5)

    def test_from_roman_known_values(self):
        '''from_roman should give known result with known input'''
        for integer, numeral in self.known_values:
            result = roman5.from_roman(numeral)
            self.assertEqual(integer, result)

if __name__ == '__main__':
    unittest.main()