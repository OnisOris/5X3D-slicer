from plane import Triangle
from threeDTool import *
from line import Line
vertexes = [[2, 0, 4],
           [4, 3, 8],
           [6, 2, 1]]
tr = Triangle(vertexes)
tr.set_barycenter()
tr.line_segments_create()
logger.debug(tr.barycenter)
x = 1
y = 1
z = tr.projection_z(x, y)
test_point = np.array([x, y, z])
tr.point_analyze(test_point)
# print(tr.get_N())
# p = vector_from_two_points([0, 3, 2.5], [4, 1, 5])
# line = Line(0, 3, 2.5, p[0], p[1], p[2])
#
# p_t = line_triangle_intersection(line, tr)
# logger.debug(p_t)
# point_in_plane(tr, p_t)

