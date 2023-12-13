import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_id_assignment(self):
        Base._Base__nb_objects = 0
        b_1 = Base()
        b_2 = Base()
        b_3 = Base()
        self.assertEqual(b_1.id, 1)
        self.assertEqual(b_2.id, 2)
        self.assertEqual(b_3.id, 3)

    def test_id_assign_next(self):
        bone = Base()
        btwo = Base()
        bthree = Base(13)
        self.assertEqual(bone.id, 1)
        self.assertEqual(btwo.id, 2)
        self.assertEqual(bthree.id, 13)

    def test_id_assign_passed(self):
        bfour = Base(15)
        self.assertEqual(bfour.id, 15)

if __name__ == '__main__':
    unittest.main()
