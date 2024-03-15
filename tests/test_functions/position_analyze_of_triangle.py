from threeDTool import position_analyze_of_triangle
from parser_stl import Parser_stl
from plane import Triangle, Plane
path = "C:\\Users\\mixai\\OneDrive - ITMO UNIVERSITY\\code\\5X3D-slicer\\cube.stl"
file = open(path, "r")
parser = Parser_stl()
triangles, name = parser.parse_stl(file)
print(triangles[0])
tr = Triangle(triangles[0])
plane = Plane(0, 1, 0, 0)
# Тест функции на треугольник перед плоскостью. Вернуть должен 1
# пройден
print(position_analyze_of_triangle(triangles[0], plane))

plane2 = Plane(0, 1, 0, -2)
# Тест функции на треугольник за плоскостью. Вернуть должен -1
# пройден
print(position_analyze_of_triangle(triangles[0], plane2))

# Тест функции на треугольник в плоскости. Вернуть должен 0
plane3 = Plane(0, 1, 0, -1)
# пройден
print(position_analyze_of_triangle(triangles[0], plane3))

# Тест функции на пересечение плоскости треугольником. Вернуть должен 2
plane4 = Plane(0, 0, 1, -0.5)
# пройден
print(position_analyze_of_triangle(triangles[0], plane4))

# Тест функции на пересечение плоскости треугольником одной вершиной. Вернуть должен -2
plane5 = Plane(0, 0, 1, 0)
# пройден
print(position_analyze_of_triangle(triangles[0], plane5))
