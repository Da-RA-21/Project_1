import math


def circle(radius: float) -> float:
    """
    Takes a value for a circle's radius and calculates area from that value
    :param radius: float value for circle's radius
    :return: The circle's area
    """
    if isinstance(radius, str) or isinstance(radius, bool):
        print('(circle) use a number!')
        raise TypeError

    if radius <= 0:
        print('(circle) radius cannot be less than one!!')
        raise ValueError

    a_of_c = math.pi * radius ** 2
    return a_of_c


def square(base: float) -> float:
    """
    Takes a value for a square's side and calculates area from that value
    :param base: float value for square's side
    :return: area of the square
    """
    if isinstance(base, str) or isinstance(base, bool):
        print('(square) use a number!')
        raise TypeError

    if base <= 0:
        print('(square) side cannot be less than one!')
        raise ValueError

    a_of_s = base ** 2
    return a_of_s


def rectangle(base: float, height: float) -> float:
    """
    takes a rectangle's base and height as arguments and calculates the area from those values
    :param base: value of the base of the rectangle
    :param height: value of the height of the rectangle
    :return: value of the area of the rectangle
    """
    if (isinstance(base, str) or isinstance(base, bool)) or (isinstance(height, str) or isinstance(height, bool)):
        print('(rectangle) use a number!')
        raise TypeError

    if base <= 0 or height <= 0:
        print('(rectangle) base or height cannot be less than one!')
        raise ValueError

    a_of_r = base * height
    return a_of_r


def triangle(base: float, height: float) -> float:
    """
    takes a triangle's base and height as arguments and calculates the area from those values
    :param base: value of the base of the triangle
    :param height: value of the height of the triangle
    :return: value of the area of the rectangle
    """
    if (isinstance(base, str) or isinstance(base, bool)) or (isinstance(height, str) or isinstance(height, bool)):
        print('(triangle) use a number!')
        raise TypeError

    if base <= 0 or height <= 0:
        print('(triangle) base or height cannot be less than one!')
        raise ValueError

    a_of_t = (1/2) * (base * height)
    return a_of_t
