import numpy as np
from loguru import logger
import matplotlib.pyplot as plt
from line import Line
from math import sqrt

class Plane:
    # coefficients - коэффициенты уравнения плоскости a, b, c, d
    def __init__(self, a=0, b=0, c=1, d=0):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d

    #
    def create_plane3(self, matrix):
        '''

        :param matrix:
        :return:
        '''
        G = np.array([[-1], [-1], [-1]])
        logger.debug(np.linalg.inv(matrix))
        abc = np.dot(np.linalg.inv(matrix), G)
        logger.debug(abc.T[0])
        coefficients = np.array([abc.T[0][0], abc.T[0][1], abc.T[0][2], 1])
        logger.debug(coefficients)
        self.__a = coefficients[0]
        self.__b = coefficients[1]
        self.__c = coefficients[2]
        self.__d = coefficients[3]
        return coefficients
        # ^ y
        # |

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
    def d(self):
        return self.__d

    @a.setter
    def a(self, a):
        self.__a = a

    @b.setter
    def b(self, b):
        self.__b = b

    @c.setter
    def c(self, c):
        self.__c = c
    @d.setter
    def d(self, d):
        self.__d = d

    def create_plane_from_triangle(self, triangle, point=1) -> None:
        """
        Данная функция принимает массив 4x3. Строка 1 - координаты вектора нормали (пишутся координаты только второй
        точки, первая исходит из нуля).
        Строки 2, 3, 4 - координаты вершин треугольника формата [x, y, z]
        На основе четырех точек создается плоскость и коэффициенты a, b, c, d записываются в поля объекта класса Plane
        Согласно параграфу 123 "Уравнение плоскости", плоскость, проходящая через точку M_0 (x_0, y_0, z_0) и
        перпендикулярная вектору N{a, b, c}, представляется уравнением:
        A(x - x_0) + B(y - y_0) + C(z - z_0) = 0 или Ax + By + Cz + D = 0,
        где D = -Ax_0 - By_o - Cz_0
        Поэтому мы берем первую вершину треугольника (по умолчанию point=1) и вектор нормали и на основе
        него создаем уравнение плоскости.
        :return: None
        """
        vector_N = triangle[0]
        mod = sqrt(vector_N[0]**2+vector_N[1]**2+vector_N[2]**2)
        # Из-за неточного экспорта в STL и вычислений в Python модуль не будет точно равен 1,
        # но должен быть примерно равен 1
        if mod <= 0.998 or mod >= 1:
            logger.warning("Модуль вектора vector_N меньше 0.998 или больше 1")
        first_point = triangle[point]
        self.__a, self.__b, self.__c = vector_N[0], vector_N[1], vector_N[2]
        #  Вычисление коэффициента D
        self.__d = self.__a*first_point[0] - self.__b*first_point[1] - self.__c*first_point[2]


    ###################
    #       0         # hight
    ################### ->
    # lenth          x
    def show(self):
        hight = 20  # Высота прямоугольника
        lenth = 20 # Длина прямоугольника
        # x = [lenth, -lenth]
        # y = [hight, -hight]
        # z = [self.projection_z()]
        x1 = -lenth / 2
        y1 = hight / 2
        point1 = np.array([x1, y1, self.projection_z(x1, y1)])
        x2 = lenth / 2
        y2 = hight / 2
        point2 = np.array([x2, y2, self.projection_z(x2, y2)])
        x3 = lenth / 2
        y3 = -hight / 2
        point3 = np.array([x3, y3, self.projection_z(x3, y3)])
        x4 = -lenth / 2
        y4 = -hight / 2
        point4 = np.array([x4, y4, self.projection_z(x4, y4)])

        matrix_x_y_z = self.full_vstack([point1, point2, point3, point4, point1]).T
        points = np.array([[x1, y1, 0], [x2, y2, 0], [x3, y3, 0], [x4, y4, 0], [x1, y1, 0]])
        matrix_points = self.full_vstack(points).T
        logger.debug(matrix_x_y_z)
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        figure = ax.plot(matrix_x_y_z[0], matrix_x_y_z[1], matrix_x_y_z[2], c='r')
        figure2 = ax.plot(matrix_points[0], matrix_points[1], matrix_points[2], c='g')

        points_proj = np.array([[points[0], point1],
                                [points[1], point2],
                                [points[2], point3],
                                [points[3], point4]])
        #logger.debug(points_proj)
        figures = []
        for i in range(4):
            figures.append(ax.plot(points_proj[i].T[0], points_proj[i].T[1], points_proj[i].T[2], c='b'))
        # figure3 = ax.plot(points_proj[0], points_proj[1], points_proj[2], c='b')

        plt.show()

    def projection_z(self, point_x, point_y):
        if self.__c == 0:
            return Exception
        point_z = (-self.__a * point_x - self.__b * point_y - self.__d) / self.__c
        return point_z

    def projection_y(self, point_x, point_z):
        if self.__b == 0:
            return Exception
        point_y = (-self.__a * point_x - self.__c * point_z - self.__d) / self.__b
        return point_y

    def projection_x(self, point_x, point_y):
        if self.__a == 0:
            return Exception
        point_x = (-self.__a * point_x - self.__b * point_y - self.__d) / self.__a
        return point_x

    def full_vstack(self, vector):
        entry_point = vector[0]
        for element in vector:
            entry_point = np.vstack([entry_point, element])
        return entry_point

    # взять любое решение из системы уравнений двух плоскостей (взять какую-нибудь координату равной например 1,
    # только проверить перпендикулярность векторов нормали плоскостей к оси, координату которой мы берем за ноль)
    # def line_from_planes(self, plane1, plane2):
    #     p1 = plane1.b * plane2.c - plane2.b * plane1.c
    #     p2 = plane1.c * plane2.a - plane2.c * plane1.a
    #     p3 = plane1.a * plane2.b - plane2.a * plane1.b
    #     # как найти точку с прямой?
    #     # Если векто
    #     z = 0
    #     x = (plane1.b*plane2.b)*(plane2.d-plane1.d)/(plane1.a*plane2.b-plane2.a*plane1.b)
    #     y = -(plane2.a*plane1.b*(plane2.d-plane1.d)/(plane1.a*plane2.b-plane2.a*plane1.b))
    #     line = Line(x, y, z, p1, p2, p3)
    #     # TODO: реализовать варианты, когда две плоскости параллельны оси z
    #     return line
