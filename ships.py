class Coordinate:
    def __init__(self, x, y):
        self.wounded = False
        self.x = x
        self.y = y

    def setWounded(self):
        self.wounded = True


class ShipSingle:
    def __init__(self, coordinate):
        self.coordinate = coordinate

    def damage(self, coordinate):
        if coordinate == self.coordinate:
            self.coordinate.setWounded()

    def is_killed(self):
        if self.coordinate.wounded:
            return True
        return False


class ShipDouble(ShipSingle):
    def __init__(self, coordinate, coordinate_second):
        super().__init__(coordinate)
        self.coordinate_second = coordinate_second

    def damage(self, coordinate):
        if self.coordinate == coordinate:
            self.coordinate.setWounded()

        if self.coordinate_second == coordinate:
            self.coordinate_second.setWounded()

    def is_killed(self):
        if self.coordinate.wounded \
                and self.coordinate_second.wounded:
            return True
        return False


class ShipThree(ShipDouble):
    def __init__(self, coordinate, coordinate_second, coordinate_third):
        super().__init__(coordinate, coordinate_second)
        self.coordinate_third = coordinate_third

    def damage(self, coordinate):
        if self.coordinate == coordinate:
            self.coordinate.setWounded()

        if self.coordinate_second == coordinate:
            self.coordinate_second.setWounded()

        if self.coordinate_third == coordinate:
            self.coordinate_third.setWounded()

    def is_killed(self):
        if self.coordinate.wounded \
                and self.coordinate_second.wounded \
                and self.coordinate_third.wounded:
            return True
        return False


class ShipFour(ShipThree):
    def __init__(self, coordinate, coordinate_second, coordinate_third, coordinate_fourth):
        super().__init__(coordinate, coordinate_second, coordinate_third)
        self.coordinate_fourth = coordinate_fourth

    def damage(self, coordinate):
        if self.coordinate == coordinate:
            self.coordinate.setWounded()

        if self.coordinate_second == coordinate:
            self.coordinate_second.setWounded()

        if self.coordinate_third == coordinate:
            self.coordinate_third.setWounded()

        if self.coordinate_fourth == coordinate:
            self.coordinate_fourth.setWounded()

    def is_killed(self):
        if self.coordinate.wounded and self.coordinate_second.wounded \
                and self.coordinate_third.wounded \
                and self.coordinate_fourth.wounded:
            return True
        return False
