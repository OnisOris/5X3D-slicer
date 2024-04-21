from surface import Sphere
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from loguru import logger
# mpl.use('TkAgg')
mpl.use('Qt5Agg')

a = 0
b = 0
c = 0

r = 1

x = 0.5
y = 0.5
z = 0.5

eq = (x-a)**2 + (y - b)**2 + (z - c)**2

point = [x, y, z]

sphere = Sphere(a, b, c, r)

print(sphere.point_analyze(point))

x = np.linspace(-r, r, 40)
y = np.linspace(-r, r, 40)
z = np.linspace(-r, r, 40)
x_m, y_m, z_m = np.meshgrid(x, y, z)
# logger.debug(x_m.reshape(-1))
x_m = x_m.reshape(-1)
y_m = y_m.reshape(-1)
z_m = z_m.reshape(-1)

XYZ = np.vstack([x_m, y_m])
XYZ = np.vstack([XYZ, z_m])
logger.debug(np.shape(XYZ))
arr = sphere.array_analyze(XYZ.T)
# logger.debug(arr)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(arr.T[0], arr.T[1], arr.T[2], color='green', s=10, marker='o')
plt.show()
