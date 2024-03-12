# from plane import Plane
from line import Line
import numpy as np
from loguru import logger
from math import sqrt

def check_position_lines(line1: Line, line2: Line) -> int:
    '''

    :param line1:
    :param line2:
    :return: 0 - если линии не компланарны, 1 - если прямые компланарны параллельны, 2 - если прямые компланарны и не параллельны
    '''
    line3 = Line()
    line3.line_create_from_points(line1.coeffs()[0:3], line2.coeffs()[0:3])
    # Проверка на компланарность. Если определитель трех векторов равен нулю, то они находятся в одной плоскости.
    arr = np.array([line3.coeffs()[3:6],
                    line1.coeffs()[3:6],
                    line2.coeffs()[3:6]])
    var = np.linalg.det(arr)
    if var == 0:
        cross = np.linalg.norm(np.cross(line1.coeffs()[3:6], line2.coeffs()[3:6]))
        # logger.debug(cross)
        if cross == 0:
            # прямые параллельны
            return 1
        else:
            # прямые не параллельны
            return 2
    else:
        # прямые не компланарны
        return 0


def point_from_line_line_intersection(line1, line2):
    # Проверка на пренадлежность одной плоскости

    # проверка:
    var = check_position_lines(line1, line2)
    # logger.debug(f"var = {var}")
    if var == 2:
        # logger.debug((line1.p2 * line2.b - line1.b * line2.p2) / (line1. p2 - line2.p2))
        x = (line1.p1 * line2.a - line1.a * line2.p1) / (line1.p1 - line2.p1)
        y = (line1.p2 * line2.b - line1.b * line2.p2) / (line1.p2 - line2.p2)
        z = (line1.p3 * line2.c - line1.c * line2.p3) / (line1.p3 - line2.p3)
        return np.array([x, y, z])


def point_from_plane_line_intersection(line, plane) -> np.ndarray or None:
    """
    Функция находит координаты точки пересечения линии line и плоскости plane.
    :param line:
    :param plane:
    :return: [x, y, z] or None
    """
    # Проверка на параллельность линии плоскости
    vector_n = np.array([plane.a, plane.b, plane.c])
    vector_line = np.array([line.p1, line.p2, line.p3])
    # logger.debug(np.dot(vector_n, vector_line))
    if np.dot(vector_n, vector_line) != 0:
        t = -(plane.a * line.a + plane.b * line.b + plane.c * line.c + plane.d) / (
                plane.a * line.p1 + plane.b * line.p2 + plane.c * line.p3)
        # logger.debug(t)
        x = t * line.p1 + line.a
        y = t * line.p2 + line.b
        z = t * line.p3 + line.c
        return np.array([x, y, z])
    else:
        logger.debug("Прямая параллельная плоскости")
        return None


def max_min_points(triangles):
    """
    Функция принимает массив из координат треугольников и возвращает минимальные максимальные точки x, y, z в виде
    списка max = [x_max, y_max, z_max], min = [x_min, y_min, z_min]
    :param triangles:
    :return: [x_max, y_max, z_max], [x_min, y_min, z_min]
    """
    # logger.debug(np.max(triangles))
    x = np.array([])
    y = np.array([])
    z = np.array([])
    for i in range(triangles.shape[0]):
        x = np.append(x, triangles[:][i].T[0][1:4])
        y = np.append(y, triangles[:][i].T[1][1:4])
        z = np.append(z, triangles[:][i].T[2][1:4])
    max_xyz = [np.max(x), np.max(y), np.max(z)]
    min_xyz = [np.min(x), np.min(y), np.min(z)]
    return max_xyz, min_xyz


def position_analyzer_of_point(point, plane) -> int:
    """
    Функция принимает точку в виде списка [x, y, z] и плоскость класса Plane. Функция говорит, по какую сторону от
    плоскости лежит точка.
    1 - точка находится перед плоскостью (куда смотрит нормаль плоскости);
    0 - точка лежит на плоскости;
    -1 - точка лежит за плоскостью (в противоположную сторону от направления нормали).
    :param point:
    :param plane:
    :return: 1, 0, -1
    """
    var = plane.a * point[0] + plane.b * point[1] + plane.c * point[2] + plane.d
    if var > 0:
        return 1
    if var < 0:
        return -1
    else:
        return 0

def position_analyzer_of_line_and_plane(line, plane):
    '''
    Функция анализирует положение линии относительно плоскости. Линия может быть: параллельна плоскости, лежать в ней,
    пересекать плоскость в точке.
    :param line:
    :param plane:
    :return: 0, если линия пренадлежит плоскости, 1, если линия параллельна плоскости и не принадлежит ей, 2, если
    линия не параллельна плоскости и пересекает ее в какой-то точке
    '''
    # Если var1 == 0 и var2 == 1, то линия либо в плоскости, если var1 != 0 и var2 == 1, то линия не в плоскости и
    # параллельна ей, если var2 != 1, то линия пересекает плоскость
    var1 = plane.a*line.a + plane.b*line.b + plane.c*line.c + plane.d
    var2 = np.linalg.norm(np.cross(line.coeffs()[3:6], plane.get_N()))
    logger.debug(f"var1 = {var1}, var2 = {var2}")
    if var1 == 0 and var2 == 1:
        return 0
    elif var1 != 0 and var2 == 1:
        return 1
    elif var2 != 1:
        return 2
    else:
        logger.error("Что-то пошло не так, таких ситуаций в реальности не существует")



def position_analyze_of_triangle(triangle, plane) -> int:
    """
    Функция принимает массив треугольников 4x3, где строка 1 - вектор нормали, строки 2-4 - это координаты вершин
    треугольников и плоскость класса Plane и говорит о местоположении треугольника относительно этой плоскости.
    Возвращает код в виде четырех чисел:
    2 - треугольник пересекает плоскость;
    1 - треугольник находится перед плоскостью (куда смотрит нормаль плоскости);
    0 - треугольник лежит в плоскости;
    -1 - треугольник лежит за плоскостью (в противоположную сторону от направления нормали).
    -2 - только одна вершина треугольника лежит в плоскости
    :param triangle:
    :param plane:
    :return: 2, 1, 0, -1
    """
    point1 = triangle[1]
    point2 = triangle[2]
    point3 = triangle[3]
    var1 = position_analyzer_of_point(point1, plane)
    var2 = position_analyzer_of_point(point2, plane)
    var3 = position_analyzer_of_point(point3, plane)
    if var1 == 1 and var2 == 1 and var3 == 1:
        return 1
    elif var1 == -1 and var2 == -1 and var3 == -1:
        return -1
    elif var1 == 0 and var2 == 0 and var3 == 0:
        return 0
    elif var1 == 0 and var2 == 1 and var3 == 1 or var1 == 0 and var2 == -1 and var3 == -1\
            or var1 == 1 and var2 == 0 and var3 == 1 or var1 == -1 and var2 == 0 and var3 == -1\
            or var1 == 1 and var2 == 1 and var3 == 0 or var1 == -1 and var2 == -1 and var3 == 0:
        return -2
    else:
        return 2


def distance_between_two_points(point1, point2) -> float:
    """
    Данная функция берет две точки с прямой (одномерное пространство) и возвращает расстояние между ними.
    Примечание: принимает два числа float.
    :param point1:
    :param point2:
    :return: Distance between two points
    """
    array = np.sort(np.array([point1, point2]))
    if array[0] < 0 <= array[1]:
        return float(abs(array[0]) + array[1])
    elif array[0] >= 0:
        return float(array[1] - array[0])
    else:
        return float(abs(array[0]) - abs(array[1]))


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



# class ThreeDTool:
#     def __init__(self):
#         self.d = 0
