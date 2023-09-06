from plane import Plane
from line import Line
import numpy as np


class ThreeDTool:

    # (x-a)/p1 = (y-b)/p2 = (z-c)/p3
    def point_from_plane_line_intersection(self, line: Line, plane: Plane):
        t = (-plane.a * line.a - plane.b * line.b - plane.c * line.c - plane.d) * line.p1 / (
                plane.a * line.p1 + plane.b * line.p2 + plane.c * line.p3)
        x = t + line.a
        y = t + line.b
        z = t + line.c
        return np.array([x, y, z])

    # def line_from_plane_intersection(self, plane1: Plane, plane2: Plane):
    #
