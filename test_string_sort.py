import unittest
from string_sort import insertion_sort

class TestStringSort(unittest.TestCase):

    def test_mixed_case_sort(self):
        words = ["Zebra", "apple", "maRker", "marble"]
        insertion_sort(words)
        self.assertEqual(words, ["apple", "marble", "maRker", "Zebra"])

    def test_empty_list(self):
        words = []
        insertion_sort(words)
        self.assertEqual(words, [])

    def test_already_sorted(self):
        words = ["apple", "banana", "cherry"]
        insertion_sort(words)
        self.assertEqual(words, ["apple", "banana", "cherry"])

    def test_duplicates(self):
        words = ["banana", "apple", "apple", "Banana"]
        insertion_sort(words)
        self.assertEqual(words, ["apple", "apple", "Banana", "banana"])

    def test_single_element(self):
        words = ["single"]
        insertion_sort(words)
        self.assertEqual(words, ["single"])

if __name__ == "__main__":
    unittest.main()
