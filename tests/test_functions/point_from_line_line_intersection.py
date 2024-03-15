from threeDTool import *
from line import Line

line1 = Line(2, 0, 0, 0, 1, 0)
line2 = Line(0, 2, 0, 1, 0, 0)
point = point_from_line_line_intersection(line1, line2)
# Проверка пройдена (вернет 2 2 0)
logger.debug(point)

line1 = Line(2, 0, 0, 1, 0, 0)
line2 = Line(0, 2, 0, 1, 0, 0)
point = point_from_line_line_intersection(line1, line2)
# Проверка пройдена, вернет None
logger.debug(point)

line1 = Line(0, 0, 0, 1, 0, 1)
line2 = Line(0, 0, 0, 1, 0, 0)
point = point_from_line_line_intersection(line1, line2)
# Проверка пройдена, вернет (0, 0, 0)
logger.debug(point)

line1 = Line(1, 1, 1, 1, 1, 1)
line2 = Line(1, 1, 1, 0, 1, 0)
point = point_from_line_line_intersection(line1, line2)
# Проверка пройдена, вернет (1, 1, 1)
logger.debug(point)

line1 = Line(1, 1, 1, 0.7071067811865476, 0.7071067811865476, 0)
line2 = Line(-1, -1, 0, 0.6666666666666666, 0.6666666666666666, 0.3333333333333333)
point = point_from_line_line_intersection(line2, line1)
# Проверка пройдена, вернет [1. 1.  1.]
logger.debug(point)
