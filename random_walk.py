from random import choice

class RandomWalk:
    """Class for generate random walk"""

    def __init__(self, num_points=5000):
        """Initialized random walk attributes"""
        self.num_points = num_points

        # All walks start from point (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all walking points"""

        # Steps calculate to need length
        while len(self.x_values) < self.num_points:

            # Define direction and walk distance
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Deviation zero walk
            if x_step == 0 and y_step == 0:
                continue

            # Define next x and y values
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)