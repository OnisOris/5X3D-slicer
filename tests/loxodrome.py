from matplotlib . pyplot import *
from ThreeDTool import *

mpl.use('Qt5Agg')
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
ax.plot(arr_T[0], arr_T[1], arr_T[2])
ax.plot(arr2_T[0], arr2_T[1], arr2_T[2])
ax.plot(arr3_T[0], arr3_T[1], arr3_T[2])
ax.plot(arr4_T[0], arr4_T[1], arr4_T[2])
ax.plot(arr5_T[0], arr5_T[1], arr5_T[2])

ax.set_xlabel(r'x ')
ax.set_ylabel(r'y ')
ax.set_zlabel( r'z ')

plt.show()
