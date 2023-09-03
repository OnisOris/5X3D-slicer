import numpy as np
from loguru import logger
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from plane import Plane
from parser_stl import Parser_stl

path = "cube.stl"
file = open(path, "r")
parser = Parser_stl()
triangles, name = parser.parse_stl(file)
#parser.show(triangles)
plane = Plane(9, 6, 3, 50)
plane.show()
# logger.debug(triangles[0][1:4])
# plane.crete_plane3(triangles[0][1:4])
