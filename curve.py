import numpy as np


class Curve():
    """
    Класс представляет траекторию в 3D пространстве
    """

    def __init__(self, curve_array):
        self.__curve_array = curve_array

    @property
    def curve_array(self):
        return self.__curve_array

    @curve_array.setter
    def curve_array(self, curve_array):
        self.__curve_array = curve_array

    def show(self, ax):
        ax.plot(self.curve_array.T[0], self.curve_array.T[1], self.curve_array.T[2])

    def __getitem__(self, item):
        return self.curve_array[item]

    def union(self, curve):
        self.curve_array = np.vstack((self.curve_array, curve.curve_array))
