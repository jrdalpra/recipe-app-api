from django.test import TestCase
from app.calc import add, subtract


class CalcTests(TestCase):

    def test_add(self):
        """Checking if I know how to write a add method"""
        self.assertEquals(add(1, 1), 2)

    def test_subtract_numbers(self):
        """Checking if I know how to write a subtract method"""
        self.assertEquals(subtract(10, 2), 8)
