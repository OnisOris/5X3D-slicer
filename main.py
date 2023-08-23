import numpy as np
from loguru import logger

path = "./cube.stl"
file = open(path, "r")


def parse_stl(file):
    text = file.read()
    index_space = text.find(" ")
    first_n = text.find("\n")
    name = text[index_space + 1:first_n]
    triangles = text.split("facet normal")[1:]
    triangles_array = np.array([])
    for id, triangle in enumerate(triangles):
        t = triangle.split("\n")
        normals_text = t[0][1:].split(" ")
        normal = np.array([])
        for norm in normals_text:
            normal = np.hstack([normal, float(norm)])
        vertex = t[2:5]
        vertex_array = normal
        for vert in vertex:
            index = vert.find("vertex") + 9
            coordinates = np.array(vert[index:].split(" "))
            coordinates = coordinates.astype(float)
            vertex_array = np.vstack([vertex_array, coordinates])
        vertex_array = np.array([vertex_array])
        if id == 0:
            triangles_array = vertex_array
        else:
            triangles_array = np.vstack([triangles_array, vertex_array])
    return triangles_array, name


triangles, name = parse_stl(file)
logger.debug(f"{len(triangles)} треугольников")
logger.debug(triangles)
logger.debug(name)
