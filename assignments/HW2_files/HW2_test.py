"""Test program for CSE-41273 Homework 2.
    Put this in the same directory as your HW2.py,
    then run it from the command line:
    python HW2_test.py

    NOTE that you can test individual exercises by giving the name
    of the test class in this format:
    python HW2_test.py -k <test_class_name>

    Where <test_class_name> is any one of:
    PairSumsTests
    WordsWithLetterTests
    PowerListTests
    RotateListTests
    GetVowelNamesTests
    AlternatingTests
    GetWordCodesTests
"""
import unittest

from HW2 import (
    pair_sums,
    words_with_letter,
    power_list,
    rotate_list,
    get_vowel_names,
    alternating,
    get_word_codes,
)


class PairSumsTests(unittest.TestCase):
    """Test pair_sums function."""

    # Test getting no result with good input
    def test_pair_sums_no_result(self):
        numbers = [1, 12, 7, 2, 3, 11, 4, 15, 6, 8, 9, 10]
        target_sum = 30  # too big, should get empty result
        self.assertEqual(pair_sums(numbers, target_sum), [])

    def test_pair_sums_one_result(self):
        numbers = [1, 12, 7, 2]
        target_sum = 3
        self.assertEqual(pair_sums(numbers, target_sum), [(1, 2)])

    def test_pair_sums_several_results(self):
        numbers = [1, 12, 7, 2, 3, 11, 4, 15, 6, 8, 9, 10]
        target_sum = 12
        expected = [(1, 11), (2, 10), (3, 9), (4, 8)]
        self.assertEqual(pair_sums(numbers, target_sum), expected)


class WordsWithLetterTests(unittest.TestCase):
    """Test words_with_letter function."""

    # Test 1 make sure it matches upper and lower case
    def test_words_with_letter_upper_lower(self):
        sentence = "The cow jumped over the moon"
        result = words_with_letter(sentence, 't')
        expected = ['The', 'the']
        self.assertEqual(result, expected)

    # Test 2 make sure it gets all the words and no dups
    def test_words_with_letter_all(self):
        sentence = "The cow jumped over the moon"
        expected = ['cow', 'over', 'moon']
        result = words_with_letter(sentence, 'o')
        self.assertEqual(result, expected)

    # Test 3 Return empty list if no matches
    def test_words_with_letter_none(self):
        sentence = "The cow jumped over the moon"
        expected = []
        result = words_with_letter(sentence, 'x')
        self.assertEqual(result, expected)

    # Test 4 No error if sentence is empty
    def test_words_with_letter_empty(self):
        self.assertEqual(words_with_letter('', 'a'), [])


class PowerListTests(unittest.TestCase):
    """Test power_list function."""

    def test_power_list(self):
        self.assertEqual(power_list([3, 2, 5]), [1, 2, 25])
        numbers = [78, 700, 82, 16, 2, 3, 9.5]
        self.assertEqual(
            power_list(numbers), [1, 700, 6724, 4096, 16, 243, 735091.890625])

    def test_unmodified_numbers(self):
        numbers = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        unchanged = list(numbers)
        expected = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
        pl = power_list(numbers)
        self.assertEqual(pl, expected)
        # ensure input not modified
        self.assertEqual(numbers, unchanged)


class RotateListTests(unittest.TestCase):
    """Test rotate_list function."""

    def test_rotate_number_list(self):
        numbers = [1, 2, 3, 4]
        saveit = id(numbers)
        self.assertEqual(rotate_list(numbers), 1)
        self.assertEqual(numbers, [2, 3, 4, 1])
        self.assertEqual(id(numbers), saveit)
        self.assertEqual(rotate_list(numbers), 2)
        self.assertEqual(numbers, [3, 4, 1, 2])

    def test_rotate_single_list(self):
        number = [1]
        self.assertEqual(rotate_list(number), 1)
        self.assertEqual(number, [1])

    def test_rotate_string_list(self):
        fruits = ['apples', 'grapes', 'peaches', 'apricots', 'bananas']
        self.assertEqual(rotate_list(fruits), 'apples')
        self.assertEqual(
            fruits, ['grapes', 'peaches', 'apricots', 'bananas', 'apples'])


class GetVowelNamesTests(unittest.TestCase):
    """Test get_vowel_names function."""

    def test_one_vowel_name(self):
        names = ["Alice", "Bob", "Christy", "Jules"]
        self.assertEqual(get_vowel_names(names), ["Alice"])

    def test_multiple_vowel_names(self):
        names = ["Scott", "arthur", "Jan", "Elizabeth"]
        self.assertEqual(get_vowel_names(names), ["arthur", "Elizabeth"])

    def test_empty_names(self):
        self.assertEqual(get_vowel_names([]), [])


class AlternatingTests(unittest.TestCase):
    """Test matrix_fill function."""
    # MAKE SURE INPUT LISTS ARE NOT MODIFIED
    def test_alternating4(self):
        expected = [1, 5, 2, 6, 3, 7, 4, 8]
        list1 = [1, 2, 3, 4]
        list2 = [5, 6, 7, 8]
        exp1 = list(list1)
        exp2 = list(list2)
        result = alternating(list1, list2)
        self.assertEqual(result, expected)
        self.assertEqual(list1, exp1)
        self.assertEqual(list2, exp2)

    def test_alternating3(self):
        expected = [1, 2, 3, 4, 5, 6]
        list1 = [1, 3, 5]
        list2 = [2, 4, 6]
        exp1 = list(list1)
        exp2 = list(list2)
        result = alternating(list1, list2)
        self.assertEqual(result, expected)
        self.assertEqual(list1, exp1)
        self.assertEqual(list2, exp2)

    def test_alternating1(self):
        expected = [1, 2]
        list1 = [1]
        list2 = [2]
        exp1 = list(list1)
        exp2 = list(list2)
        result = alternating(list1, list2)
        self.assertEqual(result, expected)
        self.assertEqual(list1, exp1)
        self.assertEqual(list2, exp2)


class GetWordCodesTests(unittest.TestCase):
    """Test get_word_codes function."""

    def test_get_word_codes(self):
        words = ["hello", "bye", "yes", "no", "python"]
        expected = {
            'yes': [121, 101, 115], 'hello': [104, 101, 108, 108, 111],
            'python': [112, 121, 116, 104, 111, 110], 'no': [110, 111],
            'bye': [98, 121, 101]}
        self.assertEqual(get_word_codes(words), expected)
        expected = {
            'Hello World':
            [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100]}
        self.assertEqual(get_word_codes(['Hello World']), expected)


if __name__ == "__main__":
    unittest.main()
