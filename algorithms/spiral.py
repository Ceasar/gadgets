

def rotate(x, y):
    """Rotate and x y pair clockwise."""
    if (x, y) == (1, 0):
        return 0, 1
    elif (x, y) == (0, -1):
        return 1, 0
    elif (x, y) == (-1, 0):
        return 0, -1
    elif (x, y) == (0, 1):
        return -1, 0


def spiral(s):
    """
    Print a matrix of numbers, spiraling clockwise.
    >>> spiral(3)
    1 2 3
    8 9 4
    7 6 5
    """
    nums = range(1, (s ** 2) + 1)
    d = {}
    x, y = 0, 0
    dx, dy = 1, 0
    for num in nums:
        d[x, y] = num
        new_x, new_y = x + dx, y + dy
        if not s > new_x >= 0 or not s > new_y >= 0 or (new_x, y + dy) in d:
            dx, dy = rotate(dx, dy)
        x, y = x + dx, y + dy

    for y in range(s):
        nums_to_print = [d[x, y] for x in range(s)]
        print " ".join(str(c) for c in nums_to_print)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
