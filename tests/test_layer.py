from plane import Plane, Triangle
from parser_stl import Parser_stl
from threeDTool import *
from layer import Layer

plane = Plane(1, 1, 1, 0)
shape = [1, 2, 3, 1, -1, -3]
layer = Layer(plane, shape)
print(layer.second_plane.d)