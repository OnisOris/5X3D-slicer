from plane import Triangle
from threeDTool import *
from line import Line
vertexes = [[-2.628688,  8.090116,  5.257376],
            [-7.236073,  5.257253,  4.472195],
            [-4.253227,  3.090114,  8.506542]]
tr = Triangle(vertexes)
# logger.debug(tr.barycenter)
# x = 3
# y = 1
# z = tr.projection_z(x, y)
test_point = np.array([-5.49799662,  5.49799662,  5.49799662])
logger.debug(tr.point_analyze(test_point))
# print(tr.get_N())
# p = vector_from_two_points([0, 3, 2.5], [4, 1, 5])
# line = Line(0, 3, 2.5, p[0], p[1], p[2])
#
# p_t = line_triangle_intersection(line, tr)
# logger.debug(p_t)
# point_in_plane(tr, p_t)

