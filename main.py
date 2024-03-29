import numpy as np
from loguru import logger
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from line import Line, Line_segment
from plane import Plane, Triangle
from parser_stl import Parser_stl
from threeDTool import *

# seg = Line_segment(y2=2, z2=1)
#
# print(seg.lenth)
# TODO: сделать проверку перпендикулярности нормали к треугольнику, если вектор не перпендикулярен, то все ломается
# tri = [[1, 1, 0], [5, 2, -6], [3, 4, 5]]
# tr = Triangle(tri)
# logger.debug(tr.triangle_array())
# print(tr.normal)
# logger.debug(tr.a)
# logger.debug(tr.b)
# logger.debug(tr.c)
# logger.debug(tr.d)
# logger.debug(tr.a*5+tr.b*2+tr.c*(-6)+tr.d)

x = np.arange(0, 10.5, 0.5)
y = np.cos(x)

plt.scatter(x, y)
plt.show()




# path = "cube.stl"
# file = open(path, "r")
# parser = Parser_stl()
# triangles, name = parser.parse_stl(file)
# print(name)
# parser.show(triangles)
# print(triangles[:][1].T[0][1:4])
# plane = Plane(0, 1, 0, 0)
# # plane.show()
# plane2 = Plane(2, 1, 1, 10)
# plane2.show()
# line = Line()
# line.line_from_planes(plane, plane2)
# line.info()
#
# print(line.a, line.b, line.c, line.p1, line.p2, line.p3)
#
# tool = ThreeDTool()
# line_z = Line(15, 0, 0, 0, 0, 1)
#
# logger.debug(tool.point_from_plane_line_intersection(line_z, plane2))
# tool.slice(triangles)
# import matplotlib.pyplot as plt
#
# import numpy as np
#
#
# def makeData ():
#     ra = 2
#     # Строим сетку в интервале от -10 до 10, имеющую 100 отсчетов по обоим координатам
#     x = np.linspace(-1, 1, ra)
#     y = np.linspace(-1, 1, ra)
#
#     # Создаем двумерную матрицу-сетку
#     xgrid, ygrid = np.meshgrid(x, y)
#
#     # В узлах рассчитываем значение функции
#     z = np.ones((ra, ra))
#
#     return xgrid, ygrid, z
#
#
# if __name__ == '__main__':
#     triangle = np.array([[0, 1, 0], [1, 1, 1], [1, 1, 0], [0, 1, 1]])
#     x, y, z = makeData()
#
#     fig = plt.figure()
#     ax = fig.add_subplot(projection='3d')
#     ax.set_xlabel("X", fontsize=15, color='red')
#     ax.set_ylabel("Y", fontsize=15, color='green')
#     ax.set_zlabel("Z", fontsize=15, color='blue')
#     po = np.array([[1, -1], [1, -1]])
#     # !!!
#     ax.plot_surface(x, y, z)
#
#     plt.show()



#tool = ThreeDTool()
# line = Line()
# line.line_create_from_points([0, 0, 0], [1, 4, 5])
#
# point = point_from_plane_line_intersection(line, plane)
#
# logger.debug(point)

# max, min = max_min_points(triangles)
# logger.debug(max)
# logger.debug(min)

# A = np.array([[2, 2, 2],
#               [1, 1, 1]])
# logger.debug(np.linalg.inv(A))


# logger.debug(triangles[0][1:4])
# plane.crete_plane3(triangles[0][1:4])


# import matplotlib.pyplot as plt
# import numpy as np
#
#
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
#
# # Make data
# u = np.linspace(0, 2 * np.pi, 100)
# v = np.linspace(0, np.pi, 100)
# x = 10 * np.outer(np.cos(u), np.sin(v))
# y = 10 * np.outer(np.sin(u), np.sin(v))
# z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
#
# logger.debug(z)
# # Plot the surface
# ax.plot_surface(x[0], [0], z)
#
# # Set an equal aspect ratio
# ax.set_aspect('equal')
#
# plt.show()
# a = np.array([0, 1])
# b = np.append(a, a)
# logger.debug(b)
