"""Homework 2 for CSE-41273"""
# Aaron Mau


# Function 1
def pair_sums(numbers, target_sum):
    """Given a list of numbers and a target sum, return a list of all
        pairs of the numbers in the list that add up to the target sum.
    """
    return [
        (val1, val2)
        for val1 in numbers
        for val2 in numbers
        if val1 + val2 == target_sum and val1 < val2
    ]


# Function 2
def words_with_letter(sentence, letter):
    """Given a sentence and a lowercase letter, return a list of words from
        the sentence that contain the given letter. Sentence can be mixed
        case. The sentence's case should be ignored for searching,
        but the result should have the correct case of the original word.
    """
    return [
        words
        for words in sentence.split(" ")
        if letter.lower() in words.lower()
    ]


# Function 3
def power_list(numbers):
    """Given a list of numbers, return a new list where each element is the
        corresponding element of the list to the power of its list index.
    """
    return [
        val ** index
        for index, val in enumerate(numbers)
    ]


# Function 4
def rotate_list(some_list):
    """Take a list as input and remove the first item from the list and add it
        to the end of the list. Return the item moved.
    """
    item_out = some_list[0]  # Could also return last item post-rotation
    some_list[:] = some_list[1:] + [item_out]  # Overwrite numbers
    return item_out


# Function 5
def get_vowel_names(names):
    """Return a list containing all names given that start with a vowel."""
    vowels = ["a", "e", "i", "o", "u"]  # Not y
    return [
        name
        for name in names
        if name[0].lower() in vowels
    ]


# Function 6
def alternating(iterable1, iterable2):
    """Return list of one item at a time from each given iterable,
        alternating between them.
    """
    # Keeping this in to visualize "loops" in the comp.
    # x = zip(iterable1, iterable2)
    # for both in x:
    #     print(both)
    #     for alt_item in both:
    #         print(alt_item)
    return [
        alt_item
        for both in zip(iterable1, iterable2)
        for alt_item in both
    ]


# Function 7
def get_word_codes(words):
    """Given a list of words, return a dictionary where the words are keys,
        and the value for each key is a list of the character codes of the
        letters of the word that is its key.
    """
    return {
        word: [ord(char)
               for char in word]
        for word in words
    }
