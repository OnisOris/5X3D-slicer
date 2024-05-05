from polyhedron import Polyhedron
import numpy as np
from line import Line
from parser_stl import *
from plane import Triangle
from loguru import logger
import matplotlib.pyplot as plt
import matplotlib as mpl
from threeDTool import *
from display import Dspl
mpl.use('Qt5Agg')

path = "C:/Users\mixai\OneDrive - ITMO UNIVERSITY\code/5X3D-slicer/test_models/MeshBody1_sphere.stl"

file = open(path, "r")
parser = Parser_stl()
triangles, name = parser.parse_stl(file)
file.close()

tr = np.array([])
for item in triangles:
    tr = np.hstack([tr, Triangle(item)])
dp = Dspl(tr)
dp.show()

polyhedron = Polyhedron(tr)

# point = np.array([-1, -0.7777777777777778, -0.33333333333333337])
# print(polyhedron.point_analyze(point))

arr0 = loxodrome(angle=90, R=1, count_of_rot=17, step=0.0025)
arr_T = arr0.T

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(arr_T[0], arr_T[1], arr_T[2], color='green', s=10, marker='o')
plt.show()

k = np.shape(arr0)[0]
arr = np.array([0, 0, 0])
for i, point in enumerate(arr0):
    var = polyhedron.point_analyze(point)
    logger.debug(f"Итерация {i}, из {k},{var}")
    if var:
        arr = np.vstack([arr, point])
logger.debug(arr.shape)
arr = arr[1:np.shape(arr)[0]]
arr2 = arr.T

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(arr2[0], arr2[1], arr2[2], color='green', s=10, marker='o')
# ax.plot(arr2[0], arr2[1], arr2[2])
plt.show()

