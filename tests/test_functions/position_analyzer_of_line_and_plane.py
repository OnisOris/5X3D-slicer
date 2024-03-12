from line import Line
from plane import Plane
from threeDTool import position_analyzer_of_line_and_plane
# Линия, параллельная оси y
line = Line(1, 0, 0, 0, 1, 1)
# Плоскость в осях x, y
plane = Plane(0, 0, 1, 0)

position_analyzer_of_line_and_plane(line, plane)