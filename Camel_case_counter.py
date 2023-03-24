"""Camel case word counter."""


def camel_case_word_counter(input_string: str) -> int:
    """
    Count words.

    Given input_string of concatenation of one or more words consisting of English letters
    where first word is lowercase and other words start with uppercase, count and return number
    of words. In case of empty string, return zero.

    camel_case_word_count("hello") => 1
    camel_case_word_count("") => 0
    camel_case_word_count("someMoreWordsHere") => 4

    :param input_string: camel cased string.
    :return: integer which shows number of words in camel cased string.
    """
    if input_string == "":
        return 0
    if len(input_string) == 1:
        return 1
    counter = 0
    for i in range(len(input_string)):
        if (i == 0 or input_string[i - 1].islower()) and input_string[i].isupper():
            counter += 1
    return counter + 1

if __name__ == "__main__":
    print(camel_case_word_counter("hello") == 1)
    print(camel_case_word_counter("") == 0)
    print(camel_case_word_counter("someMoreWordsHere") == 4)