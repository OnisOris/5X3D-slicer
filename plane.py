import numpy as np
from loguru import logger
import matplotlib.pyplot as plt

class Plane:
    # coefficients - коэффициенты уравнения плоскости a, b, c, d
    def __init__(self, coefficients=None):
        if coefficients is None:
            coefficients = [0, 0, 0, 0]
        self.coefficients = coefficients

    #
    def crete_plane3(self, matrix):
        G = np.array([[-1], [-1], [-1]])
        logger.debug(np.linalg.inv(matrix))
        abc = np.dot(np.linalg.inv(matrix), G)
        self.coefficients = np.array([abc[0], abc[1], abc[2], 1])
        # logger.debug(abc)
        return abc

    def show(self):
        hight = 2
        lenth = 2

        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        # figure = ax.plot(x, y, z, c='r')
        plt.show()
