# Writing the actual test cases for main.py
# Name = Indrajeet Mondal; Date = 11th October 2023
# SourceCode

import unittest
import main


class TestMain(unittest.TestCase):
    def test_add_51(self):
        test_param = 10
        result = main.add_5(test_param)
        self.assertEqual(result, 15)


if __name__ == '__main__':
    unittest.main()
