# from plane import Plane
from typing import Tuple, Any

from numpy import ndarray, dtype

from line import Line
import numpy as np
from loguru import logger
from math import sqrt
from twoDTool import *


def check_position_lines(line1: Line, line2: Line) -> int:
    """
    :param line1:
    :param line2:
    :return: 0 - если линии не компланарны, 1 - если прямые компланарны параллельны, 2 - если прямые компланарны и
    не параллельны 3, если линии совпадают
    """
    cross = np.linalg.norm(np.cross(line1.coeffs()[3:6], line2.coeffs()[3:6]))
    if ((np.array_equal(line1.coeffs()[0:3], line2.coeffs()[0:3]) and
         np.linalg.matrix_rank(np.array([line1.coeffs()[3:6], line2.coeffs()[3:6], line2.coeffs()[3:6]])) == 2)
            and cross == 0):
        return 3
    else:
        line3 = Line()
        line3.line_create_from_points(line1.coeffs()[0:3], line2.coeffs()[0:3])
        # Проверка на компланарность. Если определитель трех векторов равен нулю, то они находятся в одной плоскости.
        arr = np.array([line3.coeffs()[3:6],
                        line1.coeffs()[3:6],
                        line2.coeffs()[3:6]])
        var = np.linalg.det(arr)
        if var == 0:
            cross = np.linalg.norm(np.cross(line1.coeffs()[3:6], line2.coeffs()[3:6]))
            if cross == 0:
                # прямые параллельны
                return 1
            else:
                # прямые не параллельны
                return 2
        else:
            # прямые не компланарны
            return 0


def point_from_line_line_intersection(line1, line2, log=False):
    """
    Функция возвращает точку пересечения двух линий. В случае, если линии не параллельны или не компланарны, то вернет
    False
    :param line1:
    :param line2:
    :return: ndarray([x, y, z])
    """
    # Проверка на принадлежность одной плоскости
    var = check_position_lines(line1, line2)
    if var == 2:
        if line1.coeffs()[3] == 0 and line1.coeffs()[4] == 0 and line1.coeffs()[5] == 0:
            return None
        elif line2.coeffs()[3] == 0 and line2.coeffs()[4] == 0 and line2.coeffs()[5] == 0:
            return None
        if line2.p1 * line1.p3 != line2.p3 * line1.p1:
            # t_2^x
            t = ((line1.a * line1.p3 - line2.a * line1.p3 + line2.c * line1.p1 - line1.c * line1.p1) /
                 (line2.p1 * line1.p3 - line2.p3 * line1.p1))
        elif line2.p2 * line1.p3 != line2.p3 * line1.p2:
            # t_2^y
            t = ((line1.b * line1.p3 - line2.b * line1.p3 + line1.p2 * line2.c - line1.p2 * line1.c) /
                 (line2.p2 * line1.p3 - line2.p3 * line1.p2))
        else:
            # t_2^z
            t = ((line1.a * line1.p2 - line2.a * line1.p2 + line2.b * line1.p1 - line1.b * line1.p1) /
                 (line2.p1 * line1.p2 - line2.p2 * line1.p1))
        x = t * line2.p1 + line2.a
        y = t * line2.p2 + line2.b
        z = t * line2.p3 + line2.c
        return np.array([x, y, z])
    else:
        if log:
            logger.error("Прямые не пересекаются, либо совпадают")
        return False


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
    if np.dot(vector_n, vector_line) != 0:
        t = -(plane.a * line.a + plane.b * line.b + plane.c * line.c + plane.d) / (
                plane.a * line.p1 + plane.b * line.p2 + plane.c * line.p3)
        x = t * line.p1 + line.a
        y = t * line.p2 + line.b
        z = t * line.p3 + line.c
        return np.array([x, y, z])
    else:
        logger.debug("Прямая параллельная плоскости")
        return None


def point_from_line_segment_intersection(line, segment):
    point = point_from_line_line_intersection(line, segment)
    if point.__class__ != None.__class__:
        if segment.point_belongs_to_the_segment(point):
            return point
        else:
            return None
    else:
        return None


def point_from_beam_segment_intersection(beam, segment):
    """
    Функция возвращает точку пересечения луча и отрезка. Если луч ничего не пересекает, возвращается False.
    В качестве луча используется объект линии, где началом считается точка [a, b, c], а вектор направления [p1, p2, p3]
    :param beam: Line
    :param segment:
    :return:
    """
    point = point_from_line_line_intersection(beam, segment)
    if point.__class__ == False.__class__:
        return False
    D = - beam.a * beam.p1 - beam.b * beam.p2
    var = beam.p1 * point[0] + beam.p2 * point[1] + D
    D = - beam.a * beam.p1 - beam.b * beam.p2 - beam.c * beam.p3
    var = beam.p1 * point[0] + beam.p2 * point[1] + beam.p3 * point[2] + D
    if var >= 0:
        if point.__class__ != None.__class__:
            if segment.point_belongs_to_the_segment(point):
                return point
            else:
                return False
        else:
            return False
    else:
        return False


def perpendicular_line(line, left=False):
    """
    Функция возвращает линию перпендикулярную данной в 2D пространстве
    :param line:
    :return:
    """
    vector = line.coeffs()[3:5]
    if left:
        angle = -90
    else:
        angle = 90
    new_vector = vector_rotation(vector, angle, grad=True)
    new_line = Line(line.a, line.b, line.c, new_vector[0], new_vector[1], 0)
    return new_line


def max_min_points(triangles):
    """
    Функция принимает массив из координат треугольников и возвращает минимальные максимальные точки x, y, z в виде
    списка max = [x_max, y_max, z_max], min = [x_min, y_min, z_min]
    :param triangles:
    :return: [x_max, y_max, z_max], [x_min, y_min, z_min]
    """
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


def position_analyzer_of_point_and_plane(point, plane) -> int:
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
    var = point_in_plane(plane, point)  # plane.a * point[0] + plane.b * point[1] + plane.c * point[2] + plane.d
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
    var1 = plane.a * line.a + plane.b * line.b + plane.c * line.c + plane.d
    var2 = np.linalg.norm(np.cross(line.coeffs()[3:6], plane.get_N()))
    if var1 == 0 and var2 == 1:
        return 0
    elif var1 != 0 and var2 == 1:
        return 1
    elif var2 != 1:
        return 2
    else:
        logger.error("Что-то пошло не так, таких ситуаций в реальности не существует")


def position_analyze_of_triangle(triangle, plane) -> tuple[int, None] | tuple[int, Any] | tuple[
    int, ndarray[Any, dtype[Any]]]:
    """
    Функция принимает массив треугольников 4x3, где строка 1 - вектор нормали, строки 2-4 - это координаты вершин
    треугольников и плоскость класса Plane и говорит о местоположении треугольника относительно этой плоскости.
    Возвращает код в виде четырех чисел:
    2, None - треугольник пересекает плоскость (две вершины лежат в плоскости - считается за пересечение);
    1, None - треугольник находится перед плоскостью (куда смотрит нормаль плоскости);
    0, None - треугольник лежит в плоскости;
    -1, None - треугольник лежит за плоскости
    -2, [x, y, z] - только одна вершина треугольника лежит в плоскости
    (в противоположную сторону от направления нормали). Также возвращается точка вершины, которая лежит в плоскости.

    :param triangle:
    :param plane:
    :return: 2, 1, 0, -1
    """
    point1 = triangle[1]
    point2 = triangle[2]
    point3 = triangle[3]
    var1 = position_analyzer_of_point_and_plane(point1, plane)
    var2 = position_analyzer_of_point_and_plane(point2, plane)
    var3 = position_analyzer_of_point_and_plane(point3, plane)
    p1 = point_in_plane(plane, point1)
    p2 = point_in_plane(plane, point2)
    p3 = point_in_plane(plane, point3)
    if var1 == 1 and var2 == 1 and var3 == 1:
        return 1, None
    elif var1 == -1 and var2 == -1 and var3 == -1:
        return -1, None
    elif var1 == 0 and var2 == 0 and var3 == 0:
        return 0, None
    elif var1 == 0 and var2 == 1 and var3 == 1 or var1 == 0 and var2 == -1 and var3 == -1 \
            or var1 == 1 and var2 == 0 and var3 == 1 or var1 == -1 and var2 == 0 and var3 == -1 \
            or var1 == 1 and var2 == 1 and var3 == 0 or var1 == -1 and var2 == -1 and var3 == 0:
        if p1 == 0:
            return -2, point1
        elif p2 == 0:
            return -2, point2
        elif p3 == 0:
            return -2, point3
        else:
            return -2, None  # Такого варианта не должно быть, если произошло - ошибка в вычислениях
    else:
        if (var1 == -1 and var2 == -1) or (var1 == 1 and var2 == 1) or (var1 == 0 and var2 == 0):
            return 2, np.array([[point1, point3],
                                [point2, point3]])
        elif (var2 == -1 and var3 == -1) or (var2 == 1 and var3 == 1) or (var2 == 0 and var3 == 0):
            return 2, np.array([[point2, point1],
                                [point3, point1]])
        elif (var1 == -1 and var3 == -1) or (var1 == 1 and var3 == 1) or (var1 == 0 and var3 == 0):
            return 2, np.array([[point1, point2], [point3, point2]])
        else:
            logger.error("Такого случая не должно быть")


def point_in_plane(plane, point):
    var = plane.a * point[0] + plane.b * point[1] + plane.c * point[2] + plane.d
    return var


def distance_between_two_points(point1, point2) -> float:
    """
    Данная функция берет две точки с прямой (одномерное пространство) и возвращает расстояние между ними.
    Примечание: принимает два числа float.
    TODO: перепроверить
    :param point1:
    :param point2:
    :return: Distance between two points
    """
    array = np.sort(np.array([point1, point2]))
    # logger.debug(array)
    if array[0] < 0 <= array[1]:
        return float(abs(array[0]) + array[1])
    elif array[0] >= 0:
        return float(array[1] - array[0])
    else:
        return float(abs(array[0]) - abs(array[1]))


def vector_from_two_points(point1, point2):
    if np.shape(point1)[0] == 3:
        vector = np.array([point2[0] - point1[0], point2[1] - point1[1], point2[2] - point1[2]])
    else:
        vector = np.array([point2[0] - point1[0], point2[1] - point1[1]])
    return vector


def normal_of_triangle(vertex1, vertex2, vertex3):
    vertex1 = np.array(vertex1)
    vertex2 = np.array(vertex2)
    vertex3 = np.array(vertex3)
    vector1 = vector_from_two_points(vertex1, vertex2)
    vector2 = vector_from_two_points(vertex1, vertex3)
    normal = np.cross(vector1, vector2)
    mod_normal = np.linalg.norm(normal)
    # Проверка на равенство длины вектора нормали единице
    if mod_normal != 1.0:
        normal = np.array([normal[0] / mod_normal, normal[1] / mod_normal, normal[2] / mod_normal])
    return normal


def lsftp(triangle, plane):
    """
     Line segment from triangle and plane или сокращенно lsftp
    :param triangle:
    :param plane:
    :return:
    """
    index_of_position = position_analyze_of_triangle(triangle, plane)


def null_vector(vector):
    """
    Функция проверяет является ли вектор нулевым
    :param vector:
    :return:
    """
    if np.sum(vector) == 0:
        return True
    else:
        return False


def point_comparison(point1, point2):
    """
    Функция проверяет равенство двух точек. В случае равенства возвращает True, иначе False
    :param point1:
    :param point2:
    :return: bool
    """
    # if np.round(point1[0], 5) == 2.66667:
    #     logger.debug(f"{point1[0]} == {point2[0]} and {point1[1]} == {point2[1]}")
    n = 7
    point1 = np.round(point1, n)
    point2 = np.round(point2, n)

    if np.shape(point1)[0] == 2:
        point1 = np.hstack([point1, 0])
    if np.shape(point2)[0] == 2:
        point2 = np.hstack([point2, 0])
    if point1[0] == point2[0] and point1[1] == point2[1] and point1[2] == point2[2]:
        # if np.round(point1[0], 5) == 2.66667:
        #     logger.error(f"{point1[0]} == {point2[0]} and {point1[1]} == {point2[1]} {point1[0] == point2[0]}")
        return True
    else:

        return False

#
