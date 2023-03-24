def sum_between_25(numbers: list) -> int:
   """
    Return the sum of the numbers in the array which are between 2 and 5.

    Summing starts from 2 (not included) and ends at 5 (not included).
    The section can contain 2 (but cannot 5 as this would end it).
    There can be several sections to be summed.

    sum_between_25([1, 3, 6, 7]) => 0
    sum_between_25([1, 2, 3, 4, 5, 6]) => 7
    sum_between_25([1, 2, 3, 4, 6, 6]) => 19
    sum_between_25([1, 3, 3, 4, 5, 6]) => 0
    sum_between_25([1, 2, 3, 4, 5, 6, 1, 2, 9, 5, 6]) => 16
    sum_between_25([1, 2, 3, 2, 5, 5, 3, 5]) => 5

    :param numbers:
    :return:
    """
   sum_numbers = 0
   is_in_section = False
   for number in numbers:
       if number == 2:
           is_in_section = True
           continue
       elif number == 5:
            is_in_section = False
            continue
       if is_in_section:
            sum_numbers += number
   return sum_numbers

if __name__ == "__main__":
    print(sum_between_25([1, 3, 6, 7]) == 0)
    print(sum_between_25([1, 2, 3, 4, 5, 6]) == 7)
    print(sum_between_25([1, 2, 3, 4, 6, 6]) == 19)
    print(sum_between_25([1, 3, 3, 4, 5, 6]) == 0)
    print(sum_between_25([1, 2, 3, 4, 5, 6, 1, 2, 9, 5, 6]) == 16)
    print(sum_between_25([1, 2, 3, 2, 5, 5, 3, 5]) == 5)