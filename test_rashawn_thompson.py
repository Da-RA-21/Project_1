import unittest
from rashawn_thompson import circle, square, triangle, rectangle
import math


class TestRashawn (unittest.TestCase):

    def test_circle(self):
        self.assertEqual(circle(5), math.pi * 25)
        self.assertEqual(circle(5.5), math.pi * 30.25)
        self.assertRaises(TypeError, circle, 'str')
        self.assertRaises(TypeError, circle, True)
        self.assertRaises(ValueError, circle, 0)
        self.assertRaises(ValueError, circle, -1)

    def test_square(self):
        self.assertEqual(square(5), 25)
        self.assertEqual(square(5.5), 30.25)
        self.assertRaises(TypeError, square, 'str')
        self.assertRaises(TypeError, square, True)
        self.assertRaises(ValueError, square, 0)
        self.assertRaises(ValueError, square, -1)

    def test_rectangle(self):
        self.assertEqual(rectangle(5, 10), 50)

        self.assertEqual(rectangle(5.5, 10.5), 57.75)
        self.assertEqual(rectangle(5.5, 10), 55)
        self.assertEqual(rectangle(5, 10.5), 52.5)

        self.assertRaises(TypeError, rectangle, 'str', 10)
        self.assertRaises(TypeError, rectangle, 5, 'str2')
        self.assertRaises(TypeError, rectangle, 'str', 'str2')

        self.assertRaises(TypeError, rectangle, True, 10)
        self.assertRaises(TypeError, rectangle, 5, True)
        self.assertRaises(TypeError, rectangle, True, False)

        self.assertRaises(ValueError, rectangle, -5, 10)
        self.assertRaises(ValueError, rectangle, 5, -10)
        self.assertRaises(ValueError, rectangle, -5, -10)

        self.assertRaises(ValueError, rectangle, 5, 0)
        self.assertRaises(ValueError, rectangle, 0, 10)
        self.assertRaises(ValueError, rectangle, 0, 0)

    def test_triangle(self):
        self.assertEqual(triangle(5, 10), 25)

        self.assertEqual(triangle(5.5, 10), 27.5)
        self.assertEqual(triangle(5, 10.5), 26.25)
        self.assertEqual(triangle(5.5, 10.5),28.875)

        self.assertRaises(TypeError, triangle, 'str', 10)
        self.assertRaises(TypeError, triangle, 5, 'str2')
        self.assertRaises(TypeError, triangle, 'str', 'str2')

        self.assertRaises(TypeError, triangle, True, 10)
        self.assertRaises(TypeError, triangle, 5, True)
        self.assertRaises(TypeError, triangle, True, False)

        self.assertRaises(ValueError, triangle, -5, 10)
        self.assertRaises(ValueError, triangle, 5, -10)
        self.assertRaises(ValueError, triangle, -5, -10)

        self.assertRaises(ValueError, triangle, 0, 10)
        self.assertRaises(ValueError, triangle, 5, 0)
        self.assertRaises(ValueError, triangle, 0, 0)


if __name__ == '__main__':
    unittest.main()
