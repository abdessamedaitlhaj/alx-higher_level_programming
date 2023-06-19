#!/usr/bin/python3
"""Test Cases for Base class"""
import unittest, os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    __doc__ = 'TestBase class for Base class'

    def test_base_init(self):
        """Check for id"""
        b0 = Base()
        b1 = Base(0)
        b2 = Base(-4)
        b3 = Base(565)
        self.assertEqual(b0.id, 1)
        self.assertEqual(b1.id, 0)
        self.assertEqual(b2.id, -4)
        self.assertEqual(b3.id, 565)

    def test_to_json_string(self):
        """Test Base to_json_string method"""
        b = Base()
        dic = {'id': 1, 'width': 3, 'x': 3, 'y': 7}
        result = b.to_json_string([dic])
        self.assertEqual(result, '[{"id": 1, "width": 3, "x": 3, "y": 7}]')
        result = b.to_json_string([])
        self.assertEqual(result, '[]')

    def test_save_to_file(self):
        """Test cases for Base save_to_file method"""
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(5, 6)
        Rectangle.save_to_file([r1, r2])
        content = '[{"id": 1, "width": 1, "height": 2, "x": 3, "y": 4}, {"id": 2, "width": 5, "height": 6, "x": 0, "y": 0}]'
        with open('Rectangle.json', 'r') as (f):
            self.assertEqual(len(f.read()), len(content))
        s1 = Square(1, 2, 3)
        s2 = Square(5)
        Square.save_to_file([s1, s2])
        content = '[{"id": 1, "size": 1, "x": 2, "y": 3}, {"id": 2, "size": 5, "x": 0, "y": 0}]'
        with open('Square.json', 'r') as (f):
            self.assertEqual(len(f.read()), len(content))

    def test_from_json_string(self):
        """Test cases for Base from_json_string method"""
        list_input = [
         {'id':89, 
          'width':10,  'height':4},
         {'id':7, 
          'width':1,  'height':7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        content = [
         {'id':89, 
          'width':10,  'height':4},
         {'id':7, 
          'width':1,  'height':7}]
        self.assertCountEqual(list_output, content)
        list_output_1 = Rectangle.from_json_string('')
        self.assertEqual(list_output_1, '[]')
        list_output_2 = Rectangle.from_json_string(None)
        self.assertEqual(list_output_2, '[]')

    def test_create(self):
        """Test cases for Base create method"""
        r1 = Rectangle(1, 2, 3, 3)
        r1_dict = r1.to_dictionary()
        r2 = (Rectangle.create)(**r1_dict)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)
        s1 = Square(4)
        s1_dict = s1.to_dictionary()
        s2 = (Square.create)(**s1_dict)
        self.assertEqual(str(s1), str(s2))
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)

    def test_load_from_file(self):
        """Test cases for Base load_from_file method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        for x in zip(list_rectangles_input, list_rectangles_output):
            self.assertEqual(str(x[0]), str(x[1]))
        else:
            s1 = Square(10, 2)
            s2 = Square(9)
            list_squares_input = [s1, s2]
            Square.save_to_file(list_squares_input)
            list_squares_output = Square.load_from_file()
            for x in zip(list_squares_input, list_squares_output):
                self.assertEqual(str(x[0]), str(x[1]))
