# from ThreeDTool.ThreeDTool.plane import Polygon_2D
from ThreeDTool import *
import matplotlib.pyplot as plt

vert = np.array([[1, 1], [2, 2], [1, 3], [2, 4], [4, 4], [4, 1]])
pol = Polygon_2D(vert)
max_x = vert.T[0].max()
min_x = vert.T[0].min()

max_y = vert.T[1].max()
min_y = vert.T[1].min()

x = np.linspace(min_x, max_x, 8)
y = np.linspace(min_y, max_y, 8)


x_m, y_m = np.meshgrid(x, y)

plt.scatter(x_m, y_m, color='green', s=40, marker='o')
plt.show()

points = np.array([x_m, y_m])

x_m = x_m.reshape(-1)
y_m = y_m.reshape(-1)
points = np.vstack([x_m, y_m])
arr = np.array([0, 0])
for i, item in enumerate(points.T):
    var = pol.point_analyze(item)
    if var:
        arr = np.vstack([arr, item])
arr = arr[1:np.shape(arr)[0]]

x_new = arr.T[0]
y_new = arr.T[1]
plt.legend('Точки внутри многоугольника')
plt.title("Многоугольник")
plt.xlabel("x")
plt.ylabel("y")

plt.grid()
plt.scatter(x_new, y_new, color='red', s=30, marker='o')
plt.show()