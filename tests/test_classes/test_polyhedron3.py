from ThreeDTool import Polyhedron, Parser_stl, Triangle, Dspl, loxodrome
import matplotlib.pyplot as plt
import matplotlib as mpl
import trimesh
import numpy as np
mpl.use('Qt5Agg')


def loxo_create(arr0, polyh):
    path = "/tests/test_functions/test_models/MeshBody1_sphere.stl"
    your_mesh = trimesh.load_mesh(path)
    k = np.shape(arr0)[0]
    arr = np.array([0, 0, 0])
    arr_not = np.array([0, 0, 0])
    for i, point in enumerate(arr0):
        var = your_mesh.contains([point])
        if var:
            arr = np.vstack([arr, point])
        else:
            arr_not = np.vstack([arr_not, point])
    arr = arr[1:np.shape(arr)[0]]
    arr_not = arr_not[1:np.shape(arr_not)[0]]
    arr2 = arr.T
    np.save('arr_not', arr_not)
    return arr2

path = "/tests/test_functions/test_models/MeshBody1_sphere.stl"
your_mesh = trimesh.load_mesh(path)

file = open(path, "r")
parser = Parser_stl()
triangles, name = parser.parse_stl(file)
file.close()
tr = np.array([])
for item in triangles:
    tr = np.hstack([tr, Triangle(item)])
dp = Dspl(tr)
dp.show()
polyhedron = Polyhedron(tr)
arr0 = loxodrome(angle=90, R = 5, count_of_rot=6, step=0.0025, point_n=np.array([8, 0, 0]))
arr_T = arr0.T
arr2 = loxodrome(R=4, angle=90, count_of_rot=17, step=0.0025, point_n=np.array([8, 0, 0]))
arr3 = loxodrome(R=3, angle=90, count_of_rot=17, step=0.0025, point_n=np.array([8, 0, 0]))
arr4 = loxodrome(R=2, angle=90, count_of_rot=17, step=0.0025, point_n=np.array([8, 0, 0]))
arr5 = loxodrome(R=1, angle=90, count_of_rot=17, step=0.0025, point_n=np.array([8, 0, 0]))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(arr_T[0], arr_T[1], arr_T[2], color='green', s=10, marker='o')
plt.show()
arr0_a = loxo_create(arr0, polyhedron)
arr2_a = loxo_create(arr2, polyhedron)
arr3_a = loxo_create(arr3, polyhedron)
arr4_a = loxo_create(arr4, polyhedron)
arr5_a = loxo_create(arr5, polyhedron)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(arr0_a[0], arr0_a[1], arr0_a[2], color='green', s=10, marker='o')
ax.scatter(arr2_a[0], arr2_a[1], arr2_a[2], color='red', s=10, marker='o')
ax.scatter(arr3_a[0], arr3_a[1], arr3_a[2], color='yellow', s=10, marker='o')
ax.scatter(arr4_a[0], arr4_a[1], arr4_a[2], color='blue', s=10, marker='o')
ax.scatter(arr5_a[0], arr5_a[1], arr5_a[2], color='purple', s=10, marker='o')
plt.show()
