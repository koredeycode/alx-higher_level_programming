#!/usr/bin/python3
"""This module contains tests for base.py"""
import unittest
from models.base import Base


class Tests(unittest.TestCase, Base):

    def test_inputted_id(self):
        b1 = Base(9)
        self.assertEqual(b1.id, 9)

    def test_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)
