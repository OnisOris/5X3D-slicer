import numpy as np
from ThreeDTool import Dspl
from ThreeDTool import Line_segment
from ThreeDTool import Points
import matplotlib as mpl
mpl.use('Qt5Agg')

p = np.array([[1, 2, 3], [3, 5, 2], [1, 6, 8], [4, 3, 0]])
points = Points(p)
line_s = Line_segment()
line_s.segment_create_from_points([0, 0, 1], [0, 0, 5])
dp = Dspl([points, line_s])
dp.show()
