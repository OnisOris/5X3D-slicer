import numpy as np
from loguru import logger
# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
from line import Line
from plane import Plane
from parser_stl import Parser_stl
from threeDTool import ThreeDTool

path = "cube.stl"
file = open(path, "r")
parser = Parser_stl()
triangles, name = parser.parse_stl(file)
parser.show(triangles)
print(triangles[:][1].T[0][1:4])
plane = Plane(0, 1, 0, 0)
# plane.show()
plane2 = Plane(2, 1, 1, 10)
plane2.show()
line = Line()
line.line_from_planes(plane, plane2)
line.info()

print(line.a, line.b, line.c, line.p1, line.p2, line.p3)

tool = ThreeDTool()
line_z = Line(15, 0, 0, 0, 0, 1)

logger.debug(tool.point_from_plane_line_intersection(line_z, plane2))
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