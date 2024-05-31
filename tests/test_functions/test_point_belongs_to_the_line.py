from ThreeDTool import Line
import numpy as np

line = Line()
line.line_create_from_points([-1.45634, -1.3677, -1], [1, 1, 1])
line.info()

p = line.coeffs()[3:6]
abc = line.coeffs()[0:3]
point = p*3+abc
print(point)

print(line.point_belongs_to_the_line(point))

