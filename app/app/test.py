"""
    Sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers_wrong(self):
        """ Test add function wrong"""
        res = calc.add(5, 2)

        self.assertNotEqual(res, 6)

    def test_add_numbers_ok(self):
        """ Test add function """
        res = calc.add(5, 2)

        self.assertEqual(res, 7)
