import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_instance_exits(self):
        Rectangle(1, 3)
        Rectangle(5, 7)
        Rectangle(9, 8, 0, 4)
        Rectangle(4, 3, 16, 1, 2)

    def test_area_exists(self):
        rect = Rectangle(1, 2)
        self.assertTrue(hasattr(rect, "area"))

    def test_str_exists(self):
        rect = Rectangle(1, 2)
        self.assertTrue(hasattr(rect, "__str__"))

    def test_display_exists(self):
        rect = Rectangle(1, 2)
        self.assertTrue(hasattr(rect, "display"))

    def test_display_without_x_y(self):
        rect = Rectangle(1, 2)
        self.assertIsNone(rect.display())

if __name__ == '__main__':
    unittest.main()
