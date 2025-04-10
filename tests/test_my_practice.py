import unittest
from practice import *

class TestListStringOperations(unittest.TestCase):

    # List Operation Tests
    def test_get_even_numbers(self):
        self.assertEqual(get_even_numbers([1, 2, 3, 4, 5, 6]), [2, 4, 6])
        self.assertEqual(get_even_numbers([7, 8, 9, 10]), [8, 10])
        self.assertEqual(get_even_numbers([1, 3, 5, 7]), [])

    def test_get_odd_numbers(self):
        self.assertEqual(get_odd_numbers([1, 2, 3, 4, 5, 6]), [1, 3, 5])
        self.assertEqual(get_odd_numbers([7, 8, 9, 10]), [7, 9])
        self.assertEqual(get_odd_numbers([2, 4, 6, 8]), [])

    def test_sum_of_list(self):
        self.assertEqual(sum_of_list([1, 2, 3, 4]), 10)
        self.assertEqual(sum_of_list([10, -10, 5, 0]), 5)
        self.assertEqual(sum_of_list([0, 0, 0]), 0)

    def test_get_max_number(self):
        self.assertEqual(get_max_number([1, 2, 3, 4]), 4)
        self.assertEqual(get_max_number([-1, -2, -3, -4]), -1)
        self.assertEqual(get_max_number([5]), 5)

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 3, 4, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(remove_duplicates([10, 10, 10]), [10])
        self.assertEqual(remove_duplicates([1, 2, 3, 1, 2, 3]), [1, 2, 3])

    def test_reverse_list(self):
        self.assertEqual(reverse_list([1, 2, 3, 4]), [4, 3, 2, 1])
        self.assertEqual(reverse_list([5, 6, 7]), [7, 6, 5])
        self.assertEqual(reverse_list([10]), [10])

    # String Operation Tests
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")
        self.assertEqual(reverse_string("a"), "a")

    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("Python"), 1)
        self.assertEqual(count_vowels("aeiou"), 5)

    def test_remove_whitespace(self):
        self.assertEqual(remove_whitespace("hello world"), "helloworld")
        self.assertEqual(remove_whitespace("Python 3.9"), "Python3.9")
        self.assertEqual(remove_whitespace(" no spaces "), "nospaces")

    def test_capitalize_first_letter(self):
        self.assertEqual(capitalize_first_letter("hello world"), "Hello World")
        self.assertEqual(capitalize_first_letter("python programming"), "Python Programming")
        self.assertEqual(capitalize_first_letter("a"), "A")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("hello"))
        self.assertTrue(is_palindrome("madam"))

    def test_find_substring(self):
        self.assertEqual(find_substring("hello world", "world"), 6)
        self.assertEqual(find_substring("Python programming", "thon"), 1)
        self.assertEqual(find_substring("Python", "java"), -1)

    def test_replace_substring(self):
        self.assertEqual(replace_substring("hello world", "world", "Python"), "hello Python")
        self.assertEqual(replace_substring("Python is great", "is", "was"), "Python was great")
        self.assertEqual(replace_substring("Python programming", "Java", "C++"), "Python programming")

if __name__ == "__main__":
    unittest.main()
