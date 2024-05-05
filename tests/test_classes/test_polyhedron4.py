from polyhedron import Polyhedron
import numpy as np
from line import Line
from parser_stl import *
from plane import Triangle
from loguru import logger
import matplotlib.pyplot as plt
import matplotlib as mpl
from display import Dspl
from threeDTool import Points
mpl.use('Qt5Agg')

path = "C:/Users\mixai\OneDrive - ITMO UNIVERSITY\code/5X3D-slicer/test_models\MeshBody1_sphere.stl"

file = open(path, "r")
parser = Parser_stl()
triangles, name = parser.parse_stl(file)
file.close()

tr = np.array([])
for item in triangles:
    tr = np.hstack([tr, Triangle(item)])

polyhedron = Polyhedron(tr)
test_point = np.load('arr_not.npy')
logger.debug(test_point.shape)
# logger.debug(tr.point_analyze(test_point))
point = test_point[2]
print(polyhedron.get_min_max())
p = Points([point])

# x = np.linspace(-1, 1, 20)
# y = np.linspace(-1, 1, 20)
# z = np.linspace(-1, 1, 20)
# x_m, y_m, z_m = np.meshgrid(x, y, z)
# # logger.debug(x_m.reshape(-1))
# x_m = x_m.reshape(-1).T
# y_m = y_m.reshape(-1).T
# z_m = z_m.reshape(-1).T
#
# points = np.vstack([x_m, y_m.T, z_m]).T
# logger.debug(points.shape)
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(x_m, y_m, z_m, color='green', s=10, marker='o')
# plt.show()
#
print(polyhedron.point_analyze(point))
dp = Dspl([polyhedron, p])

dp.show()
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(arr2[0], arr2[1], arr2[2], color='green', s=10, marker='o')
# plt.show()

