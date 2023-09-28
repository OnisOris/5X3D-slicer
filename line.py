class Line:
    # Уравнение вида:
    # (x-a)/p1 = (y-b)/p2 = (z-c)/p3
    def __init__(self, a=0, b=0, c=0, p1=0, p2=0, p3=0):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__p1 = p1
        self.__p2 = p2
        self.__p3 = p3

    @property
    def a(self):
        return self.__a
    @property
    def b(self):
        return self.__b
    @property
    def c(self):
        return self.__c
    @property
    def p1(self):
        return self.__p1
    @property
    def p2(self):
        return self.__p2
    @property
    def p3(self):
        return self.__p3

    @a.setter
    def a(self, a):
        self.__a = a
    @b.setter
    def b(self, b):
        self.__b = b
    @c.setter
    def c(self, c):
        self.__c = c
    @p1.setter
    def p1(self, p1):
        self.__p1 = p1
    @p2.setter
    def p2(self, p2):
        self.__p2 = p2
    @p3.setter
    def p3(self, p3):
        self.__p3 = p3


    # Создание коэффициентов прямой по двум точкам в пространстве.
    # Принимает точку в виде массива 1x3 объекта класса numpy.array с тремя координатами [x, y, z]
    # point1 = [x1, y1, z1]
    def line_create_from_points(self, point1, point2):
        self.__a = - point1[0]
        self.__b = - point1[1]
        self.__c = - point1[2]
        self.__p1 = point2[0] - point1[0]
        self.__p2 = point2[1] - point1[1]
        self.__p3 = point2[2] - point1[2]

# class LineSegment(Line):
#     def __init__(self, point_a, point_b):
