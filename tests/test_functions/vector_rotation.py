from ThreeDTool import *

vector1 = np.array([0.5, 5])
print(vector_rotation(vector1.T, -90, grad=True))

line = Line(1, 1, 1, -1, 1, 0)

perpendicular_line(line).info()
