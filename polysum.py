from math import *


def polysum(n, s):
    """
    :param s: int, length of side for a polygon
    :param n: int, number of sides in a polygon
    :return: The function returns the sum, rounded to 4 decimal places,
    of the area and square of the perimeter of the regular polygon.
    .
    """
    perimeter = n * s

    area = (0.25 * n * pow(s, 2)) / tan(pi / n)

    return round(area + pow(perimeter, 2), 4)


print(polysum(3, 5))
