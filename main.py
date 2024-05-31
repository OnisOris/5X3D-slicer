import trimesh
from ThreeDTool import *
import matplotlib as mpl
mpl.use('Qt5Agg')

def loxo_create(arr0, path):
    your_mesh = trimesh.load_mesh(path)
    k = np.shape(arr0)[0]
    arr = np.array([0, 0, 0])
    arr_not = np.array([0, 0, 0])
    for i, point in enumerate(arr0):
        var = your_mesh.contains([point])
        # logger.debug(f"Итерация {i}, из {k},{var}")
        if var:
            arr = np.vstack([arr, point])
        else:
            arr_not = np.vstack([arr_not, point])
    arr = arr[1:np.shape(arr)[0]]
    arr_not = arr_not[1:np.shape(arr_not)[0]]
    arr2 = arr.T
    return arr

path = "/tests/test_functions/test_models/cube.stl"

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
point_n = polyhedron.get_median_point() - [0, 0.5, 1.2]
arr = generate_loxodromes(r=rmax, point_n=point_n, steps=0.001)

f_lox = arr[0]
for i, item in enumerate(arr):
    if i == np.shape(arr)[0] - 1:
        break
    f_lox.union(arr[i + 1])

arr_new = loxo_create(f_lox.curve_array, path)

p = Points(arr_new, method='plot')

center_point = point_n
center_p = Points([center_point], s=50, color='blue')
curves = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])
for i, item in enumerate(p.xyz):
    vector_z = vector_from_two_points(center_point, item)
    if i == p.xyz.shape[0]-1:
        point5 = curves[i - 1]
    else:
        vector_x = vector_from_two_points(p.xyz[i + 1], item)
        point5 = np.hstack([item, vector_z, vector_x])

    curves = np.vstack([curves, point5])
curves = curves[1:np.shape(curves)[0]]

curves5 = Curve5x(curves, length=0.05)

items = np.hstack([tr, p, curves5, center_p])
dp5 = Dspl(items)
dp5.show()