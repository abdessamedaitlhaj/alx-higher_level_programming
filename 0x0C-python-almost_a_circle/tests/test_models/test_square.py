#!/usr/bin/python3
"""Module that defines TestSquare for Square class"""

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test class for Square class"""

    def test_init(self):
        """Test cases for init method"""
        s1 = Square(1)
        s2 = Square(1, 2, 3)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.height, 1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s2.width, 1)
        self.assertEqual(s2.height, 1)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)

        with self.assertRaises(TypeError) as e:
            s1 = Square(-1)
            self.assertEqual("width must be > 0", str(e.exception))
