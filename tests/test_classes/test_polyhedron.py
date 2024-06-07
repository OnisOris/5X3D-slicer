from ThreeDTool import Polyhedron
from ThreeDTool.parser_stl import *
from ThreeDTool import Triangle
from loguru import logger
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use('Qt5Agg')

path = "../../tests/test_functions/test_models/cube.stl"

file = open(path, "r")
parser = Parser_stl()
triangles, name = parser.parse_stl(file)
file.close()
tr = np.array([])
for item in triangles:
    tr = np.hstack([tr, Triangle(item)])
polyhedron = Polyhedron(tr)
x = np.linspace(-1, 1, 10)
y = np.linspace(-1, 1, 10)
z = np.linspace(-1, 1, 10)
x_m, y_m, z_m = np.meshgrid(x, y, z)
x_m = x_m.reshape(-1).T
y_m = y_m.reshape(-1).T
z_m = z_m.reshape(-1).T
points = np.vstack([x_m, y_m.T, z_m]).T
logger.debug(points.shape)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_m, y_m, z_m, color='green', s=10, marker='o')
plt.show()
arr = np.array([0, 0, 0])
k = np.shape(points)[0]
for i, point in enumerate(points):
    logger.debug(f"Итерация {i}, из {k}")
    if polyhedron.point_analyze(point):
        arr = np.vstack([arr, point])
logger.debug(arr.shape)
arr = arr[1:np.shape(arr)[0]]
arr2 = arr.T
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(arr2[0], arr2[1], arr2[2], color='green', s=10, marker='o')
plt.show()

