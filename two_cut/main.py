from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    def __str__(self):
        return f"({self.x}, {self.y})"


def distance(a, b):
    return sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)


def is_between(a, c, b):
    return (distance(a, c) + distance(c, b)) == distance(a, b)


def my_approach(a, b, c, d):
    print("a, b -> ", a, " - ", b)
    print("c, d -> ", c, " - ", d)

    """
    calculate lines from cuts
    y = kx + t
    k = (y2-y1)/(x2-x1)
    t = y - kx
    """
    k1 = (b.y - a.y) / (b.x - a.x)
    t1 = a.y - k1 * a.x

    k2 = (d.y - c.y) / (d.x - c.x)
    t2 = c.y - k2 * c.x

    print("k1, t1", k1, t1)
    print("k2, t2", k2, t2)

    """
    find out where if lines cross each other
    if k1 == k2, lines does not cut each other
    otherwise, x = (t2 - t1) / (k1 - k2)
    """

    if k1 == k2:
        return False
    x = (t2 - t1) / (k1 - k2)
    y = k1 * x + t1
    cross_point = Point(x, y)
    print("cross point - ", cross_point)

    """
    check if (x, y) in cut
    """
    if is_between(a, cross_point, b) and is_between(c, cross_point, d):
        return True

    return False


if __name__ == '__main__':
    result = my_approach(Point(3, 7), Point(4, 8), Point(6, 5), Point(9, 7))
    print(result)
    print()
    result = my_approach(Point(-14, -10), Point(4, 8), Point(-12, -6), Point(9, 7))
    print(result)
