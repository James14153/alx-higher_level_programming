#!/usr/bin/python3
"""
Unittest for function "max_integer[]"
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unittest class for max integer"""

    def test_module_docstring(self):
        """ checks for module docstring """
        md = __import__('6-max_integer').__doc__
        self.assertTrue(len(md) > 1)

    def test_function_docstring(self):
        """ checks for function docstring """
        fd = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(fd) > 1)

    def test_empty_list(self):
        """ checks for an empty list """
        e = []
        self.assertIsNone(max_integer(e))

    def test_no_args(self):
        """ Checks if no arguments passed to function """
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Tests for only one number in the list"""
        o = [1]
        self.assertEqual(max_integer(o), 1)

    def test_positive_end(self):
        """Tests for all positive with max at end"""
        e = [2, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(e), 50)

    def test_positive_middle(self):
        """Tests for all positive with max in middle"""
        m = [2, 10, 8, 360, 14, 50]
        self.assertEqual(max_integer(m), 360)

    def test_positive_beginning(self):
        """Tests for all positive with max at beginning"""
        b = [200, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(b), 200)

    def test_one_negative(self):
        """Tests for list with one negative number"""
        on = [200, 10, 8, -36, 14, 50]
        self.assertEqual(max_integer(on), 200)
    
    def test_all_negative(self):
        """Tests for list with all negative numbers"""
        n = [-6, -50, -75, -1, -100]
        self.assertEqual(max_integer(n), -1)

    def test_none(self):
        """ Tests for passing none as an argument """
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int_arg(self):
        """ Tests for a non int type in list """
        string = [1, 2, "Hello", 4, 5]
        with self.assertRaises(TypeError):
            max_integer(string) 

if __name__ == "__main__":
        unittest.main()
