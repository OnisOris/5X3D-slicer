from math import sqrt
from loguru import logger
from threeDTool import *


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

    def info(self) -> None:
        logger.debug(
            f'a = {self.__a}, b = {self.__b}, c = {self.__c}, p1 = {self.__p1}, p2 = {self.__p2}, p3 = {self.__p3}')

    # Создание коэффициентов прямой по двум точкам в пространстве.
    # Принимает точку в виде массива 1x3 объекта класса numpy.array с тремя координатами [x, y, z]
    # point1 = [x1, y1, z1]
    def line_create_from_points(self, point1, point2) -> None:
        '''
        Создает коэффициенты прямой по двум точкам в пространстве.
        Принимает точку в виде массива 1x3 объекта класса numpy.array с тремя координатами [x, y, z]
        :param point1: [x1, y1, z1]
        :param point2: [x2, y2, z2]
        :return: None
        '''
        self.__a = point1[0]
        self.__b = point1[1]
        self.__c = point1[2]
        # TODO: проверка на нуль
        p1 = point2[0] - point1[0]
        p2 = point2[1] - point1[1]
        p3 = point2[2] - point1[2]
        mod_N = sqrt(p1 ** 2 + p2 ** 2 + p3 ** 2)
        # Проверка на равенство длины вектора нормали единице
        if mod_N != 1.0:
            p1 = p1 / mod_N
            p2 = p2 / mod_N
            p3 = p3 / mod_N
        self.__p1 = p1
        self.__p2 = p2
        self.__p3 = p3

    def line_from_planes(self, plane1, plane2):
        '''
        Необходимо проверить следующие ситуации:
        Если plane1 перпендикулярна z и не лежит в точке z = 0, то за нуль брать y.  
        :param plane1:
        :param plane2:
        :return:
        '''

        # Векторное произведение векторов нормали n_1 b n_2
        p1 = plane1.b * plane2.c - plane2.b * plane1.c  # проверено
        p2 = plane1.c * plane2.a - plane2.c * plane1.a
        p3 = plane1.a * plane2.b - plane2.a * plane1.b
        logger.debug(f"{p1} {p2} {p3}")
        # Сначала проверяем не параллельны ли эти две плоскости:

        if p1 != 0 and p2 != 0 and p3 != 0:
            mod_p = sqrt(p1 ** 2 + p2 ** 2 + p3 ** 2)
            if mod_p != 1.0 and mod_p != 0:
                p1 = p1 / mod_p
                p2 = p2 / mod_p
                p3 = p3 / mod_p
            elif mod_p == 0:
                logger.error("P - нулевой вектор")
                return None
            self.__p1 = p1
            self.__p2 = p2
            self.__p3 = p3
            # как найти точку с прямой?
            # если прямая не параллельна x и y, мы можем занулить координату z (c = 0)
            # Но если она параллельна, то одна из плоскостей plane1 или plane 2 параллельна осям x и y, тогда необходимо
            # занулить другую координату, например x или y

            # проверяем параллельность плоскостей осям x и y

            # # Если не параллельны, то:
            # z = 0
            val1_1 = plane1.a * plane2.b - plane2.a * plane1.b
            val1_2 = plane2.a * plane1.b - plane1.a * plane2.b
            # y = 0
            val2_1 = plane2.c * plane1.a - plane1.c * plane2.a
            val2_2 = plane2.a * plane1.c - plane1.a * plane2.c
            # x = 0
            val3_1 = plane2.c * plane1.b - plane1.c * plane2.b
            val3_2 = plane2.c * plane1.b - plane1.c * plane2.b
            if val1_1 != 0 and plane2.b != 0:
                self.__c = 0
                self.__a = (plane2.d * plane1.b - plane1.d * plane2.b) / val1_1
                self.__b = - (plane2.a * self.__a + plane2.d) / plane2.b
            if val1_2 != 0 and plane2.b == 0:
                self.__c = 0
                self.__b = (plane1.a * plane2.d - plane1.d * plane2.a) / val1_2
                self.__a = - (plane2.b * self.__c + plane2.d) / plane2.a

            elif val2_1 != 0 and plane2.c != 0:
                self.__b = 0
                self.__a = (plane2.d * plane1.c - plane1.d * plane2.c) / val2_1
                self.__c = -(plane2.a * self.__a + plane2.d) / plane2.c

            elif val2_2 != 0 and plane2.a != 0:
                self.__b = 0
                self.__c = (plane1.a * plane2.d - plane2.a * plane1.d) / val2_2
                self.__a = -(plane2.c * self.__c + plane2.d) / plane2.a

            elif val3_1 != 0 and plane2.c != 0:
                self.__a = 0
                self.__b = (plane1.c * plane2.d - plane1.d * plane2.c) / val3_1
                self.__c = -(plane2.b * self.__b + plane2.d) / plane2.c
            elif val3_2 != 0 and plane2.b != 0:
                self.__a = 0
                self.__c = (plane2.b * plane1.d - plane2.d * plane1.b) / val3_2
                self.__b = -(plane2.c * self.__c + plane2.d) / plane2.b
            else:
                logger.debug("Zero Error")
        else:
            logger.debug("Плоскости не пересекаются и либо параллельны, либо совпадают")

    def point_belongs_to_the_line(self, point):
        eq1 = self.p2 * self.p3 * (point[0] - self.a) - self.p1 * self.p3 * (point[1] - self.b)
        eq2 = self.p1 * self.p3 * (point[1] - self.b) - self.p1 * self.p2 * (point[2] - self.c)
        eq3 = self.p1 * self.p2 * (point[2] - self.c) - self.p2 * self.p3 * (point[0] - self.a)
        if eq1 == 0 and eq2 == 0 and eq3 == 0:
            return True
        else:
            return False


#         Если параллельны, то z = -D/C (d и c от параллельной плоскости)
class Line_segment(Line):
    def __init__(self,a=0, b=0, c=0, p1=0, p2=0, p3=0, x1=0, y1=0, z1=0, x2=0, y2=0, z2=0):
        super().__init__(a, b, c, p1, p2, p3)
        self.point1 = [x1, y1, z1]
        self.point2 = [x2, y2, z2]
        self.lenth = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

    # def lsftp(self, triangle, plane):
    #     '''
    #      Line segment from triangle and plane или сокращенно lsftp
    #     :return:
    #     '''
    #     pat = position_analyze_of_triangle(triangle.triangle_array())
    #     # if pat == 2:
    #     #     point1 = point_from_plane_line_intersection()
    # def point_belongs_to_the_segment(self, point):
    #     eq1 = self.p2*self.p3*(point[0]-self.a) - self.p1*self.p3*(point[1]-self.b)
    #     eq2 = self.p1*self.p3*(point[1]-self.b) - self.p1*self.p2*(point[2]-self.c)
    #     eq3 = self.p1*self.p2*(point[2]-self.c) - self.p2*self.p3*(point[0]-self.a)
    #     logger.debug(eq1)
    #     logger.debug(eq2)
    #     logger.debug(eq3)
    #
    #     if eq1 == 0 and eq2 == 0 and eq3 == 0:
    #
    #     else:
    #         return False

    def inorno(self, coordinate):
        segment = [self.point1[0], self.point2[1]]
        segment.sort()

        if segment[0] <= coordinate <= segment[1] and segment[0] != segment[1]:
            return True
        elif segment[0] == segment[1]:
            logger.debug("Нулевой отрезок")
        else:
            return False
