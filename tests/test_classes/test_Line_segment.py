from line import *

seg = Line_segment(1, 1, 1, 1, 1, 1, [-1, -1, -1], [2, 2, 2])
point = np.array([0.5, 0.5, 0.5])
print(seg.point_belongs_to_the_segment(point))

seg = Line_segment(1, 1, 1, 1, 1, 1, [0, 0, 0], [2, 2, 2])
point = np.array([0.6, 0.5, 0.5])
print(seg.point_belongs_to_the_segment(point))

seg = Line_segment(1, 1, 1, 1, 1, 1, [-1, -1, -1], [2, 2, 2])
point = np.array([-0.5, -0.5, -0.5])
print(seg.point_belongs_to_the_segment(point))
