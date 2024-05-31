from ThreeDTool import Polyhedron, Parser_stl, Triangle, Dspl, generate_loxodromes, Points
import matplotlib as mpl
import trimesh
import numpy as np
mpl.use('Qt5Agg')
from loguru import logger

def loxo_create(arr0, path):
    your_mesh = trimesh.load_mesh(path)
    k = np.shape(arr0)[0]
    arr = np.array([0, 0, 0])
    arr_not = np.array([0, 0, 0])
    for i, point in enumerate(arr0):
        var = your_mesh.contains([point])
        logger.debug(f"Итерация {i}, из {k},{var}")
        if var:
            arr = np.vstack([arr, point])
        else:
            arr_not = np.vstack([arr_not, point])
    arr = arr[1:np.shape(arr)[0]]
    arr_not = arr_not[1:np.shape(arr_not)[0]]
    arr2 = arr.T
    np.save('arr_not', arr_not)
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
point_n = polyhedron.get_median_point()
arr = generate_loxodromes(r=rmax, point_n=point_n)
f_lox = arr[0]

for i, item in enumerate(arr):
    if i == np.shape(arr)[0] - 1:
        break
    f_lox.union(arr[i + 1])

dp = Dspl(tr)
dp.show()
arr_new = loxo_create(f_lox.curve_array, path)
p = Points(arr_new)
dp3 = Dspl(np.hstack([tr, p]))
dp3.show()
