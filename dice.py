from random import randint

class Dice:
    """Represent one dice"""

    def __init__(self, num_sides=6):
        """Initialized dice with default side nums = 6"""
        self.num_sides = num_sides

    def roll(self):
        """Returned random number from 1 to sides number"""
        return randint(1, self.num_sides)