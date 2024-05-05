import matplotlib.pyplot as plt
from matplotlib . pyplot import *
from numpy import *
from mpl_toolkits . mplot3d import Axes3D
import matplotlib as mpl
mpl.use('Qt5Agg')
from threeDTool import *
#
# # r = 1 # радиус
# # t = linspace (-r , r, 100)
# # Вертикальный угол
# alpha = 2*np.pi/r
# # число витков
# n = 17
# # горизонтальный угол
# beta = np.pi / (r*n)
# # Угол поворота каждого из отрезков кривой
# i = -r # i принадлежит (0, 2*r)
# phi = i*beta

# Модель неправильной локсодромы
# x = r * cos ( t ) / cosh ( m * (t - l ))
# y = r * sin ( t ) / cosh ( m * (t - l ))
# z = r * tanh ( m * (t - l ))

# def loxodrome(LEANING_ANGLE=0, R = 70, ROTCOUNT=17, FINENESS=1000):
#     # расчёт вертикального и горизонтального углов 15
#     v_angle_unit = np.pi / R / 2
#     h_angle_unit = np.pi / R * ROTCOUNT * FINENESS
#     xr = LEANING_ANGLE / 180 * np.pi
#     xrc = np.cos(xr)
#     xrs = np.sin(xr)
#     pnts = []
#     total_rot = 0
#     flg = -1  # генерация точек кривой 27
#     # i = -R
#     t = linspace(-R, R, FINENESS)
#     arr = np.array([0, 0, 0])
#
#     for i in t:
#         x = np.cos(i * v_angle_unit) * R
#         y = np.sin(i * v_angle_unit) * R
#         v = [x * np.cos(i), y, x * np.sin(i)]
#         pnt_y = v[1] * xrc - v[2] * xrs
#         pnt_z = v[2] * xrc + v[1] * xrs
#         # pnts.append([v[0], pnt_y, pnt_z])
#         arr = np.vstack([arr, [v[0], pnt_y, pnt_z]])
#     arr = arr[1:np.shape(arr)[0]]
#     return arr

arr = loxodrome(R=1)
arr2 = loxodrome(R=0.8)
arr3 = loxodrome(R=0.6)
arr4 = loxodrome(R=0.4)
arr5 = loxodrome(R=0.2)
arr_T = arr.T
arr2_T = arr2.T
arr3_T = arr3.T
arr4_T = arr4.T
arr5_T = arr5.T
# вывод графика
fig = figure()
ax = fig.add_subplot(111 , projection = '3d')
# ax.view_init (30, 60)
ax.plot(arr_T[0], arr_T[1], arr_T[2])
ax.plot(arr2_T[0], arr2_T[1], arr2_T[2])
ax.plot(arr3_T[0], arr3_T[1], arr3_T[2])
ax.plot(arr4_T[0], arr4_T[1], arr4_T[2])
ax.plot(arr5_T[0], arr5_T[1], arr5_T[2])



ax.set_xlabel(r'x ')
ax.set_ylabel(r'y ')
ax.set_zlabel( r'z ')



plt.show()