from threeDTool import *
from loguru import logger
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use('Qt5Agg')
matrixes = matrix_create([0, np.pi/3])
print(matrixes)

first_m = np.array([[1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])

logger.debug(np.round(first_m.dot(matrixes), 4))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

show_ijk(ax, matrixes)
plt.show()