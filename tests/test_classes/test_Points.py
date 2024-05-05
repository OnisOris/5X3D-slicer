from threeDTool import *
import matplotlib as mpl
import matplotlib.pyplot as plt
from display import Dspl
from line import Line, Line_segment

p = np.array([[1, 2, 3], [3, 5, 2], [1, 6, 8], [4, 3, 0]])

points = Points(p)
line_s = Line_segment()
line_s.segment_create_from_points([0, 0, 1], [0, 0, 5])

dp = Dspl([points, line_s])

dp.show()
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(arr2[0], arr2[1], arr2[2], color='green', s=10, marker='o')
# plt.show()