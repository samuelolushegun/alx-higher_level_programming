import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_assignment(self):
        r1 = Rectangle(1, 3)
        self.assertIsInstance(r1, Rectangle)
        self.assertTrue(r1.id)


if __name__ == '__main__':
    unittest.main()
