class Line:
    # Уравнение вида:
    # (x-a)/p1 = (y-b)/p2 = (z-c)/p3
    def __init__(self, a, b, c, p1, p2, p3):
        self.a = a
        self.b = b
        self.c = c
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    # Создание коэффициентов прямой по двум точкам в пространстве
    # Принимает точку в виде массива 1x3 объекта класса numpy.array с тремя координатами [x, y ,z]
    # point1 = [x1, y1, z1]
    def line_create_from_points(self, point1, point2):
        # hello world!
        self.a = -point1[0]
        self.b = -point1[1]
        self.c = -point1[2]


