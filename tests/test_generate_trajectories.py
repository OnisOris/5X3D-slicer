import numpy as np
from loguru import logger
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

from ThreeDTool.ThreeDTool import ffdj
from line import Line, Line_segment
from plane import Plane, Triangle, Polygon
from parser_stl import Parser_stl
from threeDTool import *
from display import Dspl
import ThreeDTool
xff = ffdj()


tr = trajectory_generate(h=1, line_width=0.2)
# logger.debug(tr)
# plt.plot(tr[0], tr[1], linewidth=1)
# plt.show()

ps = np.array([[0.2, -0.1, 0],
               [1, 0, 0],
               [1, 1, 0]])
pol = Polygon(ps)

points = tr.T


# points_new = np.array([[0, 0]])
# for point in points:
#     if pol.point_analyze(point):
#         points_new = np.vstack((points_new, point))
# points_new_T = points_new.T

# logger.info(f'points shape: {points_new_T[0].shape}, points shape: {points_new_T[1].shape}')
# ps = np.vstack((ps, ps[0]))
# plt.plot(ps.T[0], ps.T[1], 'red')
# plt.plot(tr[0], tr[1], c='green')
# plt.scatter(points_new_T[0], points_new_T[1])
# plt.show()

tr2 = line_segments_array_create_from_points(tr.T)
# dp = Dspl(tr2)
# dp.show()

tr3 = trajectories_intersection_create(pol, tr2)

# tr32 = line_segments_array_create_from_points(tr3)
# p = Points(tr3, s=10)
dp2 = Dspl(np.hstack([tr3, tr2, pol]))
dp2.show()
