from threeDTool import *
from line import Line

# line1 = Line(1, 0, 0, 1, 0, 0)
# line2 = Line(0, 1, 0, 1, 0, 0)
# # Компланарные параллельные векторы
# # Пройдено
# logger.debug(check_position_lines(line1, line2))

line1 = Line(1, 0, 0, 1, 0, 0)
line2 = Line(0, 1, 0, 1, 2, 0)
# Компланарные параллельные векторы
# Пройдено
logger.debug(check_position_lines(line1, line2))

line1 = Line(1, 0, 0, 1, 0, 1)
line2 = Line(0, 1, 0, 1, 2, 0)
# Некомпланарные векторы
# Пройдено
logger.debug(check_position_lines(line1, line2))

line1 = Line(1, 0, 0, 1, 0, 1)
line2 = Line(0, 1, 0, 1, 2, 0)
# Некомпланарные векторы
# Пройдено
logger.debug(check_position_lines(line1, line2))

line1 = Line(1, 0, 0, 0, -1, 0)
line2 = Line(1, 0, 0, 0, 1, 0)
# Совпадающие вектора
# Не пройдено
logger.debug(check_position_lines(line1, line2))