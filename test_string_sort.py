# Author: Ashton Lee
# Github User: ashton01L
# Date: 10/26/2024
# Description: Modify insertion sort to sort a list of strings instead of numbers. It shouldn't return anything
# it should sort the list "in place". The sorting should ignore case. For example "Zebra" should come after "apple"
# "maRker" should come after "marble", etc.
import unittest
from string_sort import insertion_sort

class TestStringSort(unittest.TestCase):
    """
    Tests cases developed to test all facets of string_sort
    """
    def test_mixed_case_sort(self):
        """
        Tests mixed case sortation
        """
        words = ["Zebra", "apple", "maRker", "marble"]
        insertion_sort(words)
        self.assertEqual(words, ["apple", "marble", "maRker", "Zebra"])

    def test_empty_list(self):
        """
        Tests empty list
        """
        words = []
        insertion_sort(words)
        self.assertEqual(words, [])

    def test_already_sorted(self):
        """
        Tests pre-sorted list
        """
        words = ["apple", "banana", "cherry"]
        insertion_sort(words)
        self.assertEqual(words, ["apple", "banana", "cherry"])

    def test_duplicates(self):
        """
        Tests when duplicates exist, despite case sensitivity
        """
        words = ["banana", "apple", "apple", "Banana"]
        insertion_sort(words)
        self.assertEqual(words, ["apple", "apple", "Banana", "banana"])

    def test_single_element(self):
        """
        Tests when only a single element exists in list
        """
        words = ["single"]
        insertion_sort(words)
        self.assertEqual(words, ["single"])

if __name__ == "__main__":
    unittest.main()
