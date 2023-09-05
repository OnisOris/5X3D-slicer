import numpy as np
from loguru import logger
import matplotlib.pyplot as plt


class Plane:
    # coefficients - коэффициенты уравнения плоскости a, b, c, d
    def __init__(self, a=0, b=0, c=1, d=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    #
    def crete_plane3(self, matrix):
        G = np.array([[-1], [-1], [-1]])
        logger.debug(np.linalg.inv(matrix))
        abc = np.dot(np.linalg.inv(matrix), G)
        logger.debug(abc.T[0])
        coefficients = np.array([abc.T[0][0], abc.T[0][1], abc.T[0][2], 1])
        logger.debug(coefficients)
        self.a = coefficients[0]
        self.b = coefficients[1]
        self.c = coefficients[2]
        self.c = coefficients[3]
        return coefficients
        # ^ y
        # |

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
        point_z = (-self.a * point_x - self.b * point_y - self.d) / self.c
        return point_z

    def projection_y(self, point_x, point_z):
        point_y = (-self.a * point_x - self.c * point_z - self.d) / self.b
        return point_y

    def projection_x(self, point_x, point_y):
        point_x = (-self.a * point_x - self.b * point_y - self.d) / self.a
        return point_x

    def full_vstack(self, vector):
        entry_point = vector[0]
        for element in vector:
            entry_point = np.vstack([entry_point, element])
        return entry_point
