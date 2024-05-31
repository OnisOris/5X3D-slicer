from ThreeDTool import Plane, Line

plane1 = Plane(0, 0, 1, 0)
plane2 = Plane(1, 0, 0, 0)

line = Line()
line.line_from_planes(plane1, plane2)
# Тест пройден
line.info()

plane1 = Plane(0, 0, 1, 0)
plane2 = Plane(1, 1, 0, 0)

line = Line()
line.line_from_planes(plane1, plane2)
# Тест пройден
line.info()
