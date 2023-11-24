import unittest
import example as ex

class TestAll(unittest.TestCase):
    def test_area(self):
        self.assertEqual(ex.circle_area(3), 3.14 * 3 ** 2)
        self.assertEqual(ex.circle_area(1), 3.14)
        self.assertEqual(ex.circle_area(0), 0)
        self.assertEqual(ex.circle_area(2.4), 3.14 * 2.5 ** 2)
