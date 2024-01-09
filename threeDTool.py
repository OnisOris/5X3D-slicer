from plane import Plane
from line import Line
import numpy as np
from loguru import logger
from math import sqrt


def point_from_line_line_intersection(line1: Line, line2: Line):
    # проверка на параллельность прямых
    var = np.dot([line1.p1, line1.p2, line1.p3], [line2.p1, line2.p2, line2.p3])
    # TODO: Сделать проверку на нахождение прямых в одной плоскости и их совпадение
    if var != 1:
        x = (line1.p1 * line2.a - line1.a * line2.p1) / (line1.p1 - line2.p1)
        y = (line1.p2 * line2.b - line1.b * line2.p2) / (line1.p2 - line2.p2)
        z = (line1.p3 * line2.c - line1.c * line2.p3) / (line1.p3 - line2.p3)
        return np.array([x, y, z])


def point_from_plane_line_intersection(line: Line, plane: Plane) -> np.ndarray or None:
    """
    Функция находит координаты точки пересечения линии line и плоскости plane.
    :param line:
    :param plane:
    :return: [x, y, z] or None
    """
    # Проверка на параллельность линии плоскости
    vector_n = np.array([plane.a, plane.b, plane.c])
    vector_line = np.array([line.p1, line.p2, line.p3])
    logger.debug(np.dot(vector_n, vector_line))
    if np.dot(vector_n, vector_line) != 0:
        t = -(plane.a * line.a + plane.b * line.b + plane.c * line.c + plane.d) / (
                plane.a * line.p1 + plane.b * line.p2 + plane.c * line.p3)
        logger.debug(t)
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
    logger.debug(np.max(triangles))
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


def position_analyzer_of_point(point, plane: Plane) -> int:
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


def position_analyze_of_triangle(triangle, plane: Plane) -> int:
    """
    Функция принимает массив треугольников 4x3, где строка 1 - вектор нормали, строки 2-4 - это координаты вершин
    треугольников и плоскость класса Plane и говорит о местоположении треугольника относительно этой плоскости.
    Возвращает код в виде четырех чисел:
    2 - треугольник пересекает плоскость;
    1 - треугольник находится перед плоскостью (куда смотрит нормаль плоскости);
    0 - треугольник лежит в плоскости;
    -1 - треугольник лежит за плоскостью (в противоположную сторону от направления нормали).
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


def slicing(triangles, thiсk=0.1):
    max_xyz, min_xyz = max_min_points(triangles)
    z_min = min_xyz[2]
    z_max = max_xyz[2]
    hight = distance_between_two_points(z_min, z_max)
    amount_of_layers = hight / thiсk
    plane_array = np.array([])
    slice_plane = Plane(0, 0, 1, -z_min)
    points = []
    # for i in range(round(amount_of_layers)):
    for triangle in triangles:
        position_index = position_analyze_of_triangle(triangle, slice_plane)
        if position_index == 2:
            # Создаем плоскость треугольника
            plane = Plane(triangle)
            # Создаем линию пересечения плоскостей треугольника и плоскости слайсинга
            line = Line()
            line.line_from_planes(plane, slice_plane)
            # Линии из вершин треугольников
            line1_2 = Line()
            line1_2.line_create_from_points(triangle[1], triangle[2])

            line2_3 = Line()
            line2_3.line_create_from_points(triangle[2], triangle[3])

            line3_1 = Line()
            line3_1.line_create_from_points(triangle[3], triangle[1])

            point1 = point_from_line_line_intersection(line, line1_2)
            point2 = point_from_line_line_intersection(line, line2_3)
            point3 = point_from_line_line_intersection(line, line3_1)
            points.append(point1)
            points.append(point2)
            points.append(point3)
    logger.debug(points)


# class ThreeDTool:
#     def __init__(self):
#         self.d = 0
