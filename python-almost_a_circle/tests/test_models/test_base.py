import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base class."""

    def test_constructor_with_id(self):
        b1 = Base(5)
        self.assertEqual(b1.id, 5)

    def test_constructor_without_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)


if __name__ == '__main__':
    unittest.main()
