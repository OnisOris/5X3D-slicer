import numpy as np
from math import sqrt
from loguru import logger

def vector_from_two_points(point1, point2):
    vector = np.array([point2[0] - point1[0], point2[1] - point1[1], point2[2] - point1[2]])
    # logger.debug(vector)
    return vector


def normal_of_triangle(vertex1, vertex2, vertex3):
    vertex1 = np.array(vertex1)
    vertex2 = np.array(vertex2)
    vertex3 = np.array(vertex3)
    vector1 = vector_from_two_points(vertex1, vertex2)
    vector2 = vector_from_two_points(vertex1, vertex3)
    normal = np.cross(vector1, vector2)
    # logger.debug(normal)
    mod_normal = np.linalg.norm(normal)
    # logger.debug(mod_normal)
    # Проверка на равенство длины вектора нормали единице
    if mod_normal != 1.0:
        normal = np.array([normal[0]/mod_normal, normal[1]/mod_normal, normal[2]/mod_normal])
        # normal[0] = normal[0] / mod_normal
        # normal[1] = normal[1] / mod_normal
        # normal[2] = normal[2] / mod_normal
    # logger.debug(np.linalg.norm(normal))
    # logger.debug(mod_normal)
    return normal
