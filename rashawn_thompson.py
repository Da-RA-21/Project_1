import math


def circle(radius):
    if isinstance(radius, str):
        print('use a number!')
        raise TypeError

    if radius <= 0:
        print('radius cannot be less than one!!')
        raise ValueError

    a_of_c = math.pi * radius ** 2
    return a_of_c


def square(base):
    if isinstance(base, str):
        print('use a number!')
        raise TypeError

    if base <= 0:
        print('side cannot be less than one!')
        raise ValueError

    a_of_s = base ** 2
    return a_of_s


def rectangle(base, height):
    if isinstance(base, str) or isinstance(height, str):
        print('use a number!')
        raise TypeError

    if base <= 0 or height <= 0:
        print('base or height cannot be less than one!')
        raise ValueError

    a_of_r = base * height
    return a_of_r


def triangle(base, height):
    if isinstance(base, str) or isinstance(height, str):
        print('use a number!')
        raise TypeError

    if base <= 0 or height <= 0:
        print('base or height cannot be less than one!')
        raise ValueError

    a_of_t = (1/2) * (base * height)
    return a_of_t
