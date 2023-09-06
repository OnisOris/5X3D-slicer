from plane import Plane


class Layer:
    def __init__(self, plane: Plane, layer_thickness=0.1):
        self.layer_thickness = layer_thickness
        self.first_plane = plane
    def create_second_plane(self, plane: Plane):
        d=0
