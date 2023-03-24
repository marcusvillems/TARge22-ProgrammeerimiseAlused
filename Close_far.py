def close_far(a: int, b: int, c: int) -> bool:
    """
    Return if one value is "close" and other is "far".

    Given three ints, a b c, return true if one of b or c is "close"
    (differing from a by at most 1),
    while the other is "far", differing from both other values by 2 or more.

    close_far(1, 2, 10) => True
    close_far(1, 2, 3) => False
    close_far(4, 1, 3) => True
    """
    close_num = abs(a - b)
    far_num = abs(a - c)
    close_and_far = False

    if close_num <= 1 and far_num >= 2:
        close_and_far = True
    elif close_num >= 2 and far_num <= 1:
        close_and_far = True

    return close_and_far

if __name__ == "__main__":
    print(close_far(1, 2, 10) == True)
    print(close_far(1, 2, 3) == False)
    print(close_far(4, 1, 3) == True)