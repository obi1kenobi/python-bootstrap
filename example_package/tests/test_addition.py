import unittest

from example_package.addition import add


class AdditionTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(5, add(2, 3))
