from ThreeDTool import Polygon_2D, vector_from_two_points
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
mpl.use('Qt5Agg')

vert = np.array([[1, 1], [2, 2], [1, 3], [2, 4], [4, 4], [4, 1]])
pol = Polygon_2D(vert)
point = [5, 0]
point = [1.3, 3]
V = vector_from_two_points(point, pol.barycenter)
fig, ax = plt.subplots()
ax.quiver(point[0], point[1], V[0], V[1], angles='xy', scale_units='xy', scale=1, color='r')
plt.scatter(pol.barycenter[0], pol.barycenter[1], color='orange', s=40, marker='o')
for item in pol.point_of_intersection(point):
    plt.scatter(item[0], item[1], color='green', s=40, marker='o')
plt.plot(pol.get_closed_vartices().T[0], pol.get_closed_vartices().T[1])
plt.legend(('Вектор луча', 'Барицентр', 'Точка(и) пересечения луча с фигурой'))
plt.title("")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
