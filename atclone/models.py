import attr

valinst = attr.validators.instance_of


@attr.s
class Airline(object):
    name = attr.ib(default='Falcon Lines', validator=valinst(str))
    money = attr.ib(default=0.0, validator=valinst(float))
    aircrafts = attr.ib(default=attr.Factory(list))
    routes = attr.ib(default=attr.Factory(list))


@attr.s
class GeoLocation(object):
    lat = attr.ib()
    lon = attr.ib()


@attr.s
class Airport(object):
    city = attr.ib(validator=valinst(str))
    population = attr.ib(validator=valinst(int))
    name = attr.ib()
    #TODO: code should be a three digits
    code = attr.ib()
    #TODO: percentage 0..1
    popularity = attr.ib()
    #TODO: lat/lon
    location = attr.ib(validator=valinst(GeoLocation))


@attr.s
class Aircraft(object):
    #TODO: str
    constructor = attr.ib()
    #TODO: str
    model = attr.ib()
    speed = attr.ib()
    fuel_consumption = attr.ib()
    fuel_tank_size = attr.ib()
    condition = attr.ib()


@attr.s
class Flight(object):
    origin = attr.ib(validator=valinst(Airport))
    destination = attr.ib(validator=valinst(Airport))
    number = attr.ib()
    aircraft = attr.ib()
    pilot = attr.ib()


@attr.s
class Player(object):
    name = attr.ib()
    money = attr.ib()
    airlines = attr.ib(default=attr.Factory(list))


@attr.s
class Route(object):
    name = attr.ib()
    #TODO: 'shuttle' or 'cycle'
    mode = attr.ib()
    airports = attr.ib(default=attr.Factory(list))
