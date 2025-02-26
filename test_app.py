"""
Module test_app
This module contains unit tests for the functions in the app module.
"""

import unittest
from app import add, multiply, divide, greet

class TestFunctions(unittest.TestCase):
    """Unit tests for functions in the app module."""

    def test_add(self):
        """Test the add function with various inputs."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
   
    def test_multiply(self):
        """Test the multiply function with various inputs."""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(0, 10), 0)

    def test_divide(self):
        """Test the divide function, including division by zero."""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(5, 0), None)
        self.assertEqual(divide(0, 5), 0)

    def test_greet(self):
        """Test the greet function with different name inputs."""
        self.assertEqual(greet("Alice"), "Hello, Alice")
        self.assertEqual(greet(""), "Hello, World!")
        self.assertEqual(greet("Bob"), "Hello, Bob")

if __name__ == "__main__":
    unittest.main()
