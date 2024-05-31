from ThreeDTool import Plane, Line, position_analyzer_of_line_and_plane
# Линия, параллельная оси y, лежащая в плоскости xy
line = Line(1, 0, 0, 0, 1, 1)
# Плоскость в осях x, y
plane = Plane(0, 0, 1, 0)
# Тест пройден, вернуло 0
print(position_analyzer_of_line_and_plane(line, plane))

line = Line(1, 0, 0, 1, 1, 1)
# Плоскость в осях x, y
plane = Plane(0, 0, 1, 0)
# Тест пройден, вернуло 0
print(position_analyzer_of_line_and_plane(line, plane))