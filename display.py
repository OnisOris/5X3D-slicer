from plane import Polygon_2D
import numpy as np
from loguru import logger
from twoDTool import *
from threeDTool import *
import matplotlib.pyplot as plt
import matplotlib as mpl
# mpl.use('TkAgg')

mpl.use('Qt5Agg')
class Dspl:
    def __init__(self, input_array):
        self.input_array = input_array
        self.fig = None
        self.ax = None
        # self.create_subplot3D()
        # input_array[0].show(self.ax)

    def create_subplot3D(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        logger.debug("fg")
    def show(self):
        for obj in self.input_array:
            obj.show(self.ax)
        # self.ax.plot(x, y, z)
        plt.show()


