import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_id_assignment(self):
        bone = Base()
        btwo = Base()
        bthree = Base(13)
        self.assertEqual(bone.id, 1)
        self.assertEqual(btwo.id, 2)
        self.assertEqual(bthree.id, 13)

if __name == '__main__':
    unittest.main()
