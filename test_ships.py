import p

coordinate1 = p.Coordinate(2, 3)
coordinate2 = p.Coordinate(3, 1)
coordinate3 = p.Coordinate(8, 5)
coordinate4 = p.Coordinate(6, 10)
coordinate5 = p.Coordinate(2, 3)
coordinate6 = p.Coordinate(4, 8)
coordinate7 = p.Coordinate(6, 7)
coordinate8 = p.Coordinate(8, 2)
coordinate9 = p.Coordinate(9, 89)
single = p.ShipSingle(coordinate1)
double = p.ShipDouble(coordinate1, coordinate4)
triple = p.ShipThree(coordinate4, coordinate3, coordinate2)
quadruple = p.ShipFour(coordinate1, coordinate2, coordinate3, coordinate9)


def miss(ship, coordinate):
    ship.damage(coordinate)
    assert not ship.is_killed()


def kick(ship, coordinate):
    ship.damage(coordinate)
    assert ship.is_killed()


def miss_two(ship, coordinate, coordinate_second):
    ship.damage(coordinate)
    ship.damage(coordinate_second)
    assert not ship.is_killed()


def wounded_two(ship, coordinate, coordinate_second):
    ship.damage(coordinate)
    ship.damage(coordinate_second)
    assert not ship.is_killed()


def kick_two(ship, coordinate, coordinate_second):
    ship.damage(coordinate)
    ship.damage(coordinate_second)
    assert ship.is_killed()


def miss_three(ship, coordinate, coordinate_second, coordinate_third):
    ship.damage(coordinate)
    ship.damage(coordinate_second)
    ship.damage(coordinate_third)
    assert not ship.is_killed()


def wounded_three(ship, coordinate, coordinate_second, coordinate_third):
    ship.damage(coordinate)
    ship.damage(coordinate_second)
    ship.damage(coordinate_third)
    assert not ship.is_killed()


def kick_three(ship, coordinate, coordinate_second, coordinate_third):
    ship.damage(coordinate)
    ship.damage(coordinate_second)
    ship.damage(coordinate_third)
    assert ship.is_killed()


def miss_four(ship, coordinate, coordinate_second, coordinate_third, coordinate_fourth):
    ship.damage(coordinate)
    ship.damage(coordinate_second)
    ship.damage(coordinate_third)
    ship.damage(coordinate_fourth)
    assert not ship.is_killed()


def wounded_four(ship, coordinate, coordinate_second, coordinate_third, coordinate_fourth):
    ship.damage(coordinate)
    ship.damage(coordinate_second)
    ship.damage(coordinate_third)
    ship.damage(coordinate_fourth)
    assert not ship.is_killed()


def kick_four(ship, coordinate, coordinate_second, coordinate_third, coordinate_fourth):
    ship.damage(coordinate)
    ship.damage(coordinate_second)
    ship.damage(coordinate_third)
    ship.damage(coordinate_fourth)
    assert ship.is_killed()


miss(single, coordinate2)
kick(single, coordinate1)
miss_two(double, coordinate2, coordinate3)
wounded_two(double, coordinate1, coordinate3)
kick_two(double, coordinate1, coordinate4)
miss_three(triple, coordinate5, coordinate1, coordinate6)
wounded_three(triple, coordinate2, coordinate4, coordinate1)
kick_three(triple, coordinate2, coordinate3, coordinate4)
miss_four(quadruple, coordinate6, coordinate5, coordinate7, coordinate8)
wounded_four(quadruple, coordinate1, coordinate3, coordinate7, coordinate8)
kick_four(quadruple, coordinate1, coordinate2, coordinate3, coordinate9)