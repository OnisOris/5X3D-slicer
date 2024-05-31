from ThreeDTool import Triangle
import numpy as np
from loguru import logger

vertexes = [[-2.628688,  8.090116,  5.257376],
            [-7.236073,  5.257253,  4.472195],
            [-4.253227,  3.090114,  8.506542]]
tr = Triangle(vertexes)
test_point = np.array([-5.49799662,  5.49799662,  5.49799662])
logger.debug(tr.point_analyze(test_point))
