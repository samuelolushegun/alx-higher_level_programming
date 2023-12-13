import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_inst(self):
        Rectangle(1, 3)
        Rectangle(5, 7)
        Rectangle(9, 8, 0, 4)
        Rectangle(4, 3, 16, 1, 2)


if __name__ == '__main__':
    unittest.main()
