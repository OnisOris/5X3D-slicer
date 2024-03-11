import numpy as np
from loguru import logger
# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
from line import Line, Line_segment
from plane import Plane, Triangle
from parser_stl import Parser_stl
from threeDTool import *

path = "../cube.stl"
file = open(path, "r")
parser = Parser_stl()
triangles, name = parser.parse_stl(file)

def slicing(triangles, thiсk=0.1):
    # Находим пограничные координаты модели:
    max_xyz, min_xyz = max_min_points(triangles)
    # Находим минимальную координату:
    z_min = min_xyz[2]
    # Находим самую высокую часть модели:
    z_max = max_xyz[2]
    # Найдем высоту модели:
    hight = distance_between_two_points(z_min, z_max)
    # Количество слоев:
    amount_of_layers = hight / thiсk

    plane_array = np.array([])
    slice_plane = Plane(0, 0, 1, -z_min)
    points = []
    # for i in range(round(amount_of_layers)):
    # Пройдемся по всем треугольникам
    for triangle in triangles:
        position_index = position_analyze_of_triangle(triangle, slice_plane)
        # logger.debug(position_index)
        if position_index == 2:
            # Создаем плоскость треугольника
            # print(triangle)
            plane = Plane()
            plane.create_plane_from_triangle(triangle)
            # Создаем линию пересечения плоскостей треугольника и плоскости слайсинга
            line = Line()
            logger.debug(f"plane1: {plane.a, plane.b, plane.c, plane.d}, slice_plane: {slice_plane.a, slice_plane.b, slice_plane.c, slice_plane.d} \n ")
            line.line_from_planes(plane, slice_plane)
            # Линии из вершин треугольников
            line1_2 = Line()
            line1_2.line_create_from_points(triangle[1], triangle[2])
            line2_3 = Line()
            line2_3.line_create_from_points(triangle[2], triangle[3])
            line3_1 = Line()
            line3_1.line_create_from_points(triangle[3], triangle[1])
            # тОЧКИ
            point1 = point_from_line_line_intersection(line, line1_2)
            point2 = point_from_line_line_intersection(line, line2_3)
            point3 = point_from_line_line_intersection(line, line3_1)
            points.append(point1)
            points.append(point2)
            points.append(point3)
            # logger.debug(point3)
    # logger.debug(points)
slicing(triangles)