# Writing the actual test cases for main.py
# Name = Indrajeet Mondal; Date = 12th October 2023
# SourceCode

import unittest
import main

class TestMain(unittest.TestCase):
    # Testing with integer input
    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    # Testing with string input
    def test_do_stuff2(self):
        test_param = 'shkshks'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    # Testing with None input
    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter an integer value')

    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter an integer value')
    
    def tearDown(self) -> None:
        print("Cleaning Up !!!")

if __name__ == '__main__':
    unittest.main()
