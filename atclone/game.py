# coding: utf-8
"""
Controller classes for my atclone live here
"""

from datetime import datetime as dt
import pytz

from . import models


class Game(object):
    """This is where the game logic lives

    All game variables are created and updated here. The only direct output
    you will find here is debug logging.
    """

    game_time = None
    start_timestamp = None
    home_airport = None
    your_start_airline = None
    you = None
    competitors = None

    def basic_setup(self):
        """Populate the game with the "standard" settings"

        This is the demo setup for a single player game
        """

        self.game_time = 0
        self.start_timestamp = dt.now(pytz.utc)
        self.home_airport = models.Airport(
            'Frankfurt', 500*1000, 'Fraport',
            'FRA', 0.90, models.GeoLocation(50.0, 8.0)
        )
        self.your_start_airline = models.Airline('Knasterraster')
        self.you = models.Player('Karl Knaster', 100*1000*1000)
        self.you.airlines.append(self.your_start_airline)
        self.competitors = [
            models.Player(
                'Jana Jodelpiep', 100*1000*1000,
                [models.Airline('Jodellines')]
            ),
            models.Player(
                'Petra Plunder', 100*1000*1000,
                [models.Airline('Plunderbar')]
            ),
            models.Player(
                'Benno Bodenlos', 100*1000*1000,
                [models.Airline('Bodenbrummer')]
            )
        ]


class ViewControl(object):
    """Kind of interface for game view

    Since there are no interfaces in python use this class as master
    to define the view elements we need in the game
    """

    def __init__(self, game):

        self.game = game

    def jour_fix(self):
        """
        The jour fix is the daily meeting where the Airport manager summarizes
        the events of the passed day
        """
        raise NotImplementedError()

    def office(self):
        """
        Entering your office. Multiple actions are waiting here for you.
        """
        raise NotImplementedError()

    def quit_game(self):
        """Time to say good-bye!"""
        raise NotImplementedError()


class CliViewControl(ViewControl):
    """Why not having a command line interface to a game?"""

    def leave(self):
        """Cli handle for leaving a room"""
        input('Press <Enter> to continue')

    def jour_fix(self):

        print(
            "[Airport Manager]: Good morning everyone. Let's get down to "
            "busines."
        )
        print(
            "\tIn {:%B %Y} we still have these Airlines at {}".format(
                self.game.start_timestamp, self.game.home_airport.name
            )
        )
        for player in self.game.competitors + [self.game.you]:
            print("\t\t{} owned by {}".format(player.airlines, player.name))
        self.leave()

    def office(self):
        print("You are entering your office")
        self.leave()

    def quit_game(self):
        print("Adios!")
        self.leave()
