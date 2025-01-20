"""Homework 1 for CSE-41273"""
# Aaron Mau
# ^^^^^^ Lines beginning with a "# " are comments.
# So, MY homework would have LINE 2 as:
# Diane Chen
#
# Please use the name you are registered under; not nicknames or alternates.
# Be sure to read the instructions that came with this file.
# If you do not follow instructions, you will not be successful.
# PLEASE ALWAYS PUT YOUR NAME ON LINE 2. DO NOT CHANGE MY ARRANGEMENT OF LINES.
# MY AUTOMATED TESTING DEPENDS UPON THIS.
#
# NOTE: The only code that should be here when you submit it are the functions.
# NOTE: There should be NO print statements anywhere when you submit the file.


# Function 1
def silly_case(sentence):
    """Given a sentence, convert it to a string such that each word starts with
        a lower case letter, and the remaining letters of the word are
        in upper case.
        Return the silly case string.
    """
    # Instructions call for no for loops, map(), list comp., or help. functions
    # Recursion - have the function call itself
    # Not sure how to consolidate the word, *rest, if rest, and return lines
    lines = sentence.splitlines()  # Start by breaking up potential poem chars
    if len(lines) > 1:
        # New line chars present
        line = lines[0]
        word, *rest = line.split(" ", 1)
        new_word = word[0].lower() + word[1:].upper()
        if rest:
            rest = silly_case(rest[0])
        line = new_word + " " + rest
        return line + "\n" + silly_case("\n".join(lines[1:]))
    else:
        # Single line (remaining)
        word, *rest = lines[0].split(" ", 1)
        new_word = word[0].lower() + word[1:].upper()
        if rest:
            return new_word + " " + silly_case(rest[0])
        else:
            # Last word
            return new_word


# Function 2
def dash_stringify(list_of_words):
    """Given a list of word strings, return a single string with all the word
        strings together, with ' - ' in between the words.
    """
    return ' - '.join(list_of_words)


# Function 3
def is_perfect_square(any_number):
    """Given any number, return True if it is a perfect square,
        else return False
    """
    # Def. perfect square: Integer that is square of an integer (i^2).
    if isinstance(any_number, int):
        # flake8 did not like type(any_number) != int:
        # Could do a int(any_number) for if strings are passed, but that might
        # require try-else stuff
        if any_number.is_integer():
            any_number = int(any_number)
        else:
            return False
    root = any_number ** (1/2)
    if root.is_integer():
        return True
    else:
        return False


# Function 4
def comfort_level(temperature):
    """Given a temperature in Fahrenheit, return a string that is a
        comment on the comfort level.
    """
    # Definitions for comfort level from instructions
    if temperature < 60:
        return "Too cold"
    elif temperature < 70:
        return "A bit chilly"
    elif temperature > 82:
        return "Too hot"
    elif temperature > 74:
        return "A bit warm"
    else:
        return "A comfortable temperature"


# Function 5
def fstring_practice(numbers, divisor):
    """Given a list of numbers and a divisor, return a list of strings:
        number divided by divisor is result
        for each number in the input list of numbers.
        You must use f-strings!
        See instructions for more details.
    """
    list_out = []
    for n in numbers:
        divided = n / divisor
        list_out.append(f"{n} divided by {divisor} is {divided}")
    return list_out


# Function 6
def string_info(sentences):
    """Given a string (multi-line probably), return a dictionary such that:
        Each key is a line number of a line of the string, starting at 1.
        The corresponding value is a tuple containing 3 items:
            the line,
            number of characters in the line,
            number of words in the line
        See the instructions for more details.
    """
    listed_sent = sentences.splitlines()
    dictionary = {}
    for i, sentence in enumerate(listed_sent, start=1):
        dictionary[i] = (sentence, len(sentence), len(sentence.split()))
    return dictionary


# Function 7
def get_earliest(date1, date2):
    """Given 2 date strings in "MM/DD/YYYY" format, return earliest one.
        DO NOT use the datetime module!
        Use string manipulation and unpacking.
    """
    mm1, dd1, yyyy1 = date1.split("/")
    mm2, dd2, yyyy2 = date2.split("/")
    if int(yyyy2) > int(yyyy1):
        return date1
    elif int(yyyy2) < int(yyyy1):
        return date2
    else:
        # The years are the same
        if int(mm2) > int(mm1):
            return date1
        elif int(mm2) < int(mm1):
            return date2
        else:
            # The months are the same
            if int(dd2) > int(dd1):
                return date1
            elif int(dd2) < int(dd1):
                return date2
            else:
                # The dates are the same to the day
                return date1
