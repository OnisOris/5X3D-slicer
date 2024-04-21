from polyhedron import Polyhedron
import numpy as np
from line import Line
from parser_stl import *
from plane import Triangle

path = "C:/Users\mixai\OneDrive - ITMO UNIVERSITY\code/5X3D-slicer/test_models\cube.stl"
file = open(path, "r")
parser = Parser_stl()
triangles, name = parser.parse_stl(file)

tr = np.array([])
for item in triangles:
    tr = np.hstack([tr, Triangle(item)])

polyhedron = Polyhedron(tr)

print(polyhedron.barycenter)
point = np.array([0.5, 0.5, 0.5])
polyhedron.point_analyze(point)
