import numpy as np
from loguru import logger
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from plane import Plane
from parser_stl import Parser_stl

path = "mainHolder.stl"
file = open(path, "r")
parser = Parser_stl()
triangles, name = parser.parse_stl(file)
parser.show(triangles)
plane = Plane(1, 1, 1, 0)
plane.show()
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