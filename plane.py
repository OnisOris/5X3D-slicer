class Plane:
    # coefficients - коэффициенты уравнения плоскости a, b, c, d
    def __init__(self, coefficients=None):
        if coefficients is None:
            coefficients = [0, 0, 0, 0]
        self.coefficients = coefficients
        