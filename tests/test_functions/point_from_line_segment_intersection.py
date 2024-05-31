import line
from ThreeDTool import threeDTool as td, Line_segment, Line

seg = Line_segment(0, 0, 0, 1, 1, 0, [-1, -1, 0], [2, 2, 0])
line = Line(0, 1, 0, 0, -1, 0)
point = td.point_from_line_segment_intersection(line, seg)
print(point)
