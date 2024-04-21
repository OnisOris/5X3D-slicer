import numpy as np
from line import Line
from loguru import logger
from threeDTool import *
class Polyhedron:
    def __init__(self, triangles):
        self.triangles = triangles
        self.__barycenter = 0
        self.set_barycenter()

    def set_barycenter(self):
        arr = np.array([0, 0, 0])
        for tr in self.triangles:
            arr = np.vstack([arr, tr.get_mean_vertexes()])
        arr = arr[1:]
        xyz_mean = arr.mean(axis=0)
        self.__barycenter = xyz_mean

    @property
    def barycenter(self):
        return self.__barycenter
    @barycenter.setter
    def barycenter(self, barycenter):
        self.__barycenter = barycenter
    def point_analyze(self, point: np.ndarray):
        line = Line()
        # tets_point = np.array(self.__barycenter)
        tets_point = np.array(self.__barycenter)
        if point_comparison(point, self.barycenter):
            tets_point += 1
        line.line_create_from_points(point, tets_point)
        line.info()
        arr = np.array([[0, 0, 0]])
        for i, item in enumerate(self.triangles):
            p = np.array(point_from_beam_segment_intersection(line, item))
            if np.shape(p) == (3,):
                arr = np.vstack([arr, p])
        arr = arr[1:np.shape(arr)[0]]
