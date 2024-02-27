import unittest
from prime import is_prime

class PrimeTestCase(unittest.TestCase):
    def test_prime_numbers(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(19))
        self.assertTrue(is_prime(23))
        self.assertTrue(is_prime(29))

    def test_non_prime_numbers(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(12))
        self.assertFalse(is_prime(14))
        self.assertFalse(is_prime(15))

    def test_negative_numbers(self):
        self.assertFalse(is_prime(-2))
        self.assertFalse(is_prime(-3))
        self.assertFalse(is_prime(-5))
        self.assertFalse(is_prime(-7))
        self.assertFalse(is_prime(-11))
        self.assertFalse(is_prime(-13))
        self.assertFalse(is_prime(-17))
        self.assertFalse(is_prime(-19))
        self.assertFalse(is_prime(-23))
        self.assertFalse(is_prime(-29))

    def test_large_prime_number(self):
        self.assertTrue(is_prime(9973))

    def test_large_non_prime_number(self):
        self.assertFalse(is_prime(9974))

if __name__ == '__main__':
    unittest.main()