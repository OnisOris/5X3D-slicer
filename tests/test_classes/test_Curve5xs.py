import trimesh
from ThreeDTool import *
import matplotlib as mpl
mpl.use('Qt5Agg')

path = "../../tests/test_functions/test_models/cube.stl"

file = open(path, "r")
parser = Parser_stl()
triangles, name = parser.parse_stl(file)
file.close()

tr = np.array([])
for item in triangles:
    tr = np.hstack([tr, Triangle(item)])

polyhedron = Polyhedron(tr)

# вычисление радиуса
r = np.array([np.linalg.norm(polyhedron.get_min_max()[0]), np.linalg.norm(polyhedron.get_min_max()[1])])
rmax = np.max(r)/2
point_n = polyhedron.get_median_point() - [0, 0.5, 0.5]
arr = generate_loxodromes(r=rmax, point_n=point_n, steps=0.001)

cc = cut_curve(arr[2], path)

center_point = point_n
center_p = Points([center_point], s=50, color='green', text=True)
curves5x = np.array([])
for curve in cc:
    out_curve = Curve5x()
    for i, item in enumerate(curve.curve_array):
        vector_z = vector_from_two_points(center_point, item)
        vector_z[0] = 0
        if i == curve.curve_array.shape[0] - 1:
            point5 = out_curve[i - 1]
        else:
            vector_x = vector_from_two_points(curve.curve_array[i + 1], item)
            vector_x[2] = 0
            point5 = np.hstack([item, vector_z, vector_x])
        out_curve.union(point5)
        angles_from_vector(point5)
    curves5x = np.hstack([curves5x, out_curve])

curves5x = np.hstack([curves5x, center_p])
dp = Dspl(curves5x)
dp.show()


