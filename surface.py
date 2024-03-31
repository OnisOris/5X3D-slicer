class Sphere:
    """
    Класс сферы. Основано на уравнении (x-a)^2 + (y - b)^2 + (z - c)^2 = r^2
    """

    def __init__(self, r, a=0, b=0, c=0):
        self.r = r
        self.a = a
        self.b = b
        self.c = c

    