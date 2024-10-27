# Author: Ashton Lee
# Github User: ashton01L
# Date: 10/26/2024
# Description: Modify insertion sort to sort a list of strings instead of numbers. It shouldn't return anything
# it should sort the list "in place". The sorting should ignore case. For example "Zebra" should come after "apple"
# "maRker" should come after "marble", etc.
def insertion_sort(a_list):
    """
    Sorts a_list of strings in ascending order, ignoring case.
    """
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        # Compare lowercase versions of the strings for case-insensitive sorting
        while pos >= 0 and a_list[pos].lower() > value.lower():
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value

# words = ["Zebra", "apple", "maRker", "marble"]
# insertion_sort(words)
# print(words)