from plane import Plane
from line import Line
import numpy as np
from loguru import logger

def point_from_plane_line_intersection(line: Line, plane: Plane):
    t = (-plane.a * line.a - plane.b * line.b - plane.c * line.c - plane.d) * line.p1 / (
            plane.a * line.p1 + plane.b * line.p2 + plane.c * line.p3)
    x = t + line.a
    y = t + line.b
    z = t + line.c
    return np.array([x, y, z])

def max_min_points(triangles):
    '''
    Функция принимает массив из координат треугольников и возвращает минимальные максимальные точки x, y, z в виде
    списка max = [x_max, y_max, z_max], min = [x_min, y_min, z_min]
    :param triangles:
    :return:
    '''
    logger.debug(np.max(triangles))
    x = np.array([])
    y = np.array([])
    z = np.array([])
    for i in range(triangles.shape[0]):
        x = np.append(x, triangles[:][i].T[0][1:4])
        y = np.append(y, triangles[:][i].T[1][1:4])
        z = np.append(z, triangles[:][i].T[2][1:4])
    max = [np.max(x), np.max(y), np.max(z)]
    min = [np.min(x), np.min(y), np.min(z)]
    return max, min
class ThreeDTool:
    def __init__(self):
        self.d = 0

    # (x-a)/p1 = (y-b)/p2 = (z-c)/p3

    # def line_from_plane_intersection(self, plane1: Plane, plane2: Plane):
    #
