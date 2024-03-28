from twoDTool import angle_from_vectors_2d, opposite_vectors
import numpy as np
v1 = [0, 4]
v2 = [1, 0]
# По часовой - положительный, против часовой - отрицательный угол
print(angle_from_vectors_2d(v1, v2)*180/np.pi)
print(angle_from_vectors_2d(v2, v1)*180/np.pi)

v1 = [1, 1]
v2 = [-1, -1]
print(angle_from_vectors_2d(v1, v2)*180/np.pi)

v1 = [1, 1]
v2 = [-1, 1]
print(angle_from_vectors_2d(v1, v2)*180/np.pi)
