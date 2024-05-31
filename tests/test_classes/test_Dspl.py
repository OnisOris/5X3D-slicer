from ThreeDTool.display import Dspl
from ThreeDTool.triangle import Triangle
from ThreeDTool.threeDTool import *
import matplotlib as mpl

mpl.use('Qt5Agg')
vertexes = [[2, 0, 4],
            [4, 3, 8],
            [6, 2, 1]]
tr = Triangle(vertexes)
tr.set_barycenter()
tr.line_segments_create()
logger.debug(tr.barycenter)
tr.point_analyze(np.array([2, 0, 4]))
line = Line_segment()
line.segment_create_from_points([0, 0, 0], [6, 2, 1])
dspl = Dspl([tr, line])
dspl.show()
