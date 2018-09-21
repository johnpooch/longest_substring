import unittest
from longest import longest


class TestLongest(unittest.TestCase):

    def test_is_this_thing_on(self):
        self.assertTrue(True)

    def test_1_from_a(self):
        self.assertEqual(longest('a'), 1)

    def test_2_from_ab(self):
        self.assertEqual(longest('ab'), 2)

    def test_2_from_aba(self):
        self.assertEqual(longest('aba'), 2)

    def test_3_from_abcabcbb(self):
        self.assertEqual(longest('abc'), 3)

    def test_1_from_bbbbb(self):
        self.assertEqual(longest('bbbbb'), 1)

    def test_3_from_pwwkew(self):
        self.assertEqual(longest('pwwkew'), 3)
