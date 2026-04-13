# https://github.com/Aureulion/lab11-TB-VN.git
# Partner 1: Veronica Nava
# Partner 2: Tyler Bauman
import unittest
#from calculator import *
from calculator import div as divide, mul as multiply, add, subtract, logarithm, exp, square_root, hypotenuse

class TestCalculator(unittest.TestCase):

    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(2,3), 6)
        self.assertEqual(multiply(-5,10), -50)
        self.assertEqual(multiply(6,11), 66)

    def test_divide(self):# 3 assertions
        self.assertAlmostEqual(divide(10,2), 0.2)
        self.assertAlmostEqual(divide(-10,2), -0.2)
        self.assertAlmostEqual(divide(2,5), 2.5)


    
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
              logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3,4), 5.0)
        self.assertAlmostEqual(hypotenuse(5,-12), 13.0)
        self.assertAlmostEqual(hypotenuse(-3,4), 5.0)


    def test_sqrt(self): # 3 assertions
        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(25), 5.0)
        with self.assertRaises(ValueError):
             square_root(-4)

    def test_add(self):  # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 4), -4)
        self.assertEqual(subtract(-2, -2), 0)

    ##########################

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            divide(0, 5)

    def test_logarithm(self):  # 3 assertions
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 10), 1)

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 10)  # base 1 is invalid


    # Do not touch this
if __name__ == "__main__":
    unittest.main()