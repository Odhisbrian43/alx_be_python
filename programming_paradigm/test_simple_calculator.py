#test module

import unittest
import simple_calculator

class SimpleCalculator(unittest.TestCase):

    def test_add(self):
        result = simple_calculator.add(5, 7)
        self.assertEqual(result, 12)

if __name__ == '__main__':
    unittest.main()
