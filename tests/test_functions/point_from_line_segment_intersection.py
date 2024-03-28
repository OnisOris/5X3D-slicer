import line
import numpy as np
import threeDTool as td

seg = line.Line_segment(0, 0, 0, 1, 1, 0, [-1, -1, 0], [2, 2, 0])
line = line.Line(0, 1, 0, 0, -1, 0)

point = td.point_from_line_segment_intersection(line, seg)

print(point)
