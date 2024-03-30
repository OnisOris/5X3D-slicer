import numpy as np
from loguru import logger
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from line import Line, Line_segment
from plane import Plane, Triangle
from parser_stl import Parser_stl
from threeDTool import *

path = "../test_models/cube.stl"
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
    points_array = []
    # Пройдем по всем слоям
    for _ in range(int(amount_of_layers)):
        # Пройдемся по всем треугольникам
        for triangle in triangles:
            position_index, points = position_analyze_of_triangle(triangle, slice_plane)
            # logger.debug(position_index)
            if position_index == 2:
                # Создаем плоскость треугольника
                # print(triangle)
                plane = Plane()
                plane.create_plane_from_triangle(triangle, create_normal=True)
                # Создаем линию пересечения плоскостей треугольника и плоскости слайсинга
                line = Line()
                line.line_from_planes(plane, slice_plane)
                # Линии из вершин треугольников
                line1 = Line()
                line1.line_create_from_points(points[0, 0], points[0, 1])
                line2 = Line()
                line2.line_create_from_points(points[1, 0], points[1, 1])
                # Точки
                point1 = point_from_line_line_intersection(line, line1)
                point2 = point_from_line_line_intersection(line, line2)
                if point1.__class__ == np.ndarray:
                    points_array.append(point1)
                if point2.__class__ == np.ndarray:
                    points_array.append(point2)
        slice_plane.d -= 0.1
    points_array = np.array(points_array)
    u, idx = np.unique(points_array, axis=0, return_index=True)
    points_array = u[idx.argsort()]
    logger.debug(points_array)
    return points_array.T

points = slicing(triangles)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(points[0], points[1], points[2])
plt.show()