from plane import Polygon_2D
import numpy as np
from loguru import logger
import matplotlib.pyplot as plt
from twoDTool import *
from threeDTool import *
import matplotlib.pyplot as plt

# vert = np.array([[-5, 0], [1, 0], [0, 1]])
# # vert = np.array([[1, 1], [2, 2], [1, 3], [2, 4], [4, 4], [4, 1]])
# pol = Polygon_2D(vert)
# point = np.array([3, 4])
# logger.debug(pol.point_analyze(point))
#
# V = vector_from_two_points(point, pol.barycenter)
# fig, ax = plt.subplots()
# ax.quiver(point[0], point[1], V[0], V[1], angles='xy', scale_units='xy', scale=1, color='r')
# plt.scatter(pol.barycenter[0], pol.barycenter[1], color='orange', s=40, marker='o')
# for item in pol.point_of_intersection(point):
#     plt.scatter(item[0], item[1], color='green', s=40, marker='o')
# plt.plot(pol.get_closed_vartices().T[0], pol.get_closed_vartices().T[1])
# plt.legend(('Вектор луча', 'Барицентр', 'Точка(и) пересечения луча с фигурой'))
# plt.title("Многоугольник")
# plt.xlabel("x")
# plt.ylabel("y")
#
# plt.grid()
# plt.show()
#
# vert = np.array([[1, 1], [2, 2], [1, 3], [2, 4], [4, 4], [4, 1]])
# pol = Polygon_2D(vert)
# point = np.array([3, 4])
# logger.debug(pol.point_analyze(point))
#
# V = vector_from_two_points(point, pol.barycenter)
# fig, ax = plt.subplots()
# ax.quiver(point[0], point[1], V[0], V[1], angles='xy', scale_units='xy', scale=1, color='r')
# plt.scatter(pol.barycenter[0], pol.barycenter[1], color='orange', s=40, marker='o')
# for item in pol.point_of_intersection(point):
#     plt.scatter(item[0], item[1], color='green', s=40, marker='o')
# plt.plot(pol.get_closed_vartices().T[0], pol.get_closed_vartices().T[1])
# plt.legend(('Вектор луча', 'Барицентр', 'Точка(и) пересечения луча с фигурой'))
# plt.title("Многоугольник")
# plt.xlabel("x")
# plt.ylabel("y")
#
# plt.grid()
# plt.show()

vert = np.array([[1, 1], [2, 2], [1, 3], [2, 4], [4, 4], [4, 1]])
pol = Polygon_2D(vert)
point = [3, 0]
logger.debug(pol.point_analyze(point))

V = vector_from_two_points(point, pol.barycenter)
fig, ax = plt.subplots()
ax.quiver(point[0], point[1], V[0], V[1], angles='xy', scale_units='xy', scale=1, color='r')
plt.scatter(pol.barycenter[0], pol.barycenter[1], color='orange', s=40, marker='o')
for item in pol.point_of_intersection(point):
    plt.scatter(item[0], item[1], color='green', s=40, marker='o')
plt.plot(pol.get_closed_vartices().T[0], pol.get_closed_vartices().T[1])
plt.legend(('Вектор луча', 'Барицентр', 'Точка(и) пересечения луча с фигурой'))
plt.title("Многоугольник")
plt.xlabel("x")
plt.ylabel("y")

plt.grid()
plt.show()